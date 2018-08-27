from django.shortcuts import render, redirect
from django.http import HttpResponse
from functools import reduce
from math import ceil, floor
from .models import File
from user.helper import login_required
import json
import time
import csv
import os
import pandas as pd

# Create your views here.


def index(request):
    return render(request, "index.html")


@login_required
def table_basic(request):
    page = int(request.GET.get('page', 1))  # 页码

    total = File.objects.count()  # 文件总数
    per_page = 15                   # 每页文件数
    pages = ceil(total / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page

    file_list = File.objects.all().order_by('-id')[start:end]
    print(len)
    data = {
            'file_list': file_list,
            'total': total,
            'pages': range(pages),
            }
    return render(request, "table_basic.html", {'data': data})


@login_required
def data(request):
    fname = request.GET.get('fname')
    data = get_data(fname)
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def pie_data(request):
    fname = request.GET.get('fname')
    data = get_data2(fname)
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def chart_line(request):
    return render(request, "chart_line.html")


@login_required
def chart_columnar(request):
    return render(request, "chart_columnar.html")


@login_required
def chart_pie(request):
    return render(request, "chart_pie.html")


@login_required
def chart_scatter(request):
    return render(request, "chart_scatter.html")


@login_required
def table_cmplete(request):
    fname = request.GET.get('fname')
    page = int(request.GET.get('page', 1))  # 页码
    per_page = 15
    request.session['fname'] = fname
    excel_data = clear_data(fname)
    len = excel_data.__len__()
    pages = ceil(len / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page
    if end >= len:
        end = len
    a = excel_data.index.tolist()
    b = []
    data1 = dict()
    for i in range(start, end):
        b.append(excel_data.iloc[i].values.tolist())
    for i, j in zip(a, b):
        data1.update({str(i+1): j})
    data2 = {'xxx': excel_data.columns.tolist()}
    data = {
            'data': data1,
            'data2': data2,
            'pages': range(pages),
            'fname': fname,
            'len': len,
            }
    return render(request, "table_complete.html", {'data': data})


@login_required
def file_upload(request):
    fpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if request.method == 'POST':
        uname = request.session.get('username')
        print(uname)
        file = request.FILES.get('file')
        if file:
            fname = file.name
            f1 = File.objects.filter(fname=fname)
            if f1:
                f1.delete()
            print(file, fname)
            fileext = fname.split(".")[1]
            with open(os.path.join('files', fname), 'wb+') as f:
                if fileext == "xlsx" or fileext == "xls":
                    data = pd.read_excel(file)
                    data.to_excel(os.path.join('files', fname), index=False)

                elif fileext == "csv":
                    data = pd.read_csv(file)
                    data.to_csv(os.path.join('files', fname), index=False, sep=',')
                else:
                    print("文件类型不支持！")
                    return redirect('/file_upload')

                date = time.localtime(time.time())
                date = time.strftime('%Y-%m-%d %H:%M:%S', date)
                f2 = File(fname=fname, fpath=fpath+'\\files\\'+fname, uname=uname, date=date)
                # 将本地文件保存到数据库
                f2.save()
                return redirect('/table_basic')
        else:
            return render(request, "file_upload.html")
    else:
        return render(request, "file_upload.html")


# 处理表格数据, 按列获取
def get_data1(fname):
    data = clear_data(fname)
    data1 = dict()
    data2 = dict()
    for i in range(len(data.columns)):
        data1.update({data.columns[i]: data[data.columns[i]].values.tolist()})
    for key, value in data1.items():
        if is_number(value[0]):
            print(str(value[0]))
            sum1 = reduce(add, value)
            data2.update({key: sum1})
        else:
            continue
    print(data2)
    return data2


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def add(x, y):
    return x+y


# 饼状图数据
def get_data2(fname):
    data = clear_data(fname)
    data1 = dict()
    for i in range(len(data.columns)):
        data1.update({data.columns[i]: data[data.columns[i]].values.tolist()})
    data3 = []
    for key, value in data1.items():
        d = {}
        if is_number(value[0]):
            # print(str(value[0]))
            sum1 = floor(reduce(add, value))
            d['Name'] = key
            d['Data'] = sum1
            data3.append(d)
        else:
            continue
        print(d)
    dd = {'list': data3}
    return dd


# def csv_data(f):


# 柱状图数据
def get_data(fname):
    f = File.objects.get(fname=fname).fpath
    ext = fname.split('.')[1]
    if f:
        dic = {}
        crr = []
        if ext == 'csv':
            with open(f, 'r') as f1:
                reader = csv.reader(f1)
                for line in reader:
                    crr.append(line)
                nrows = len(crr)
                arr = crr[0]
                for rowindex in range(1, nrows):
                        dic[rowindex] = crr[rowindex]
        else:
            data = pd.read_excel(f)
            nrows = list(data.shape)[0]
            arr = list(data)
            for i in range(nrows):
                brr = []
                d = list(data.iloc[i])
                for j in range(len(d)):
                    s = d[j]
                    if is_number(s):
                        s = float(s)
                    brr.append(s)
                crr.append(brr)
            for rowindex in range(1, nrows+1):
                    dic[rowindex] = crr[rowindex-1]

        totalArray = {
            "name": arr,
            "data": dic
        }
    return totalArray


# 读取表格
def clear_data(fname):
    f = File.objects.get(fname=fname).fpath
    ext = fname.split('.')[1]
    if f:
        if ext == 'csv':
            data = pd.read_csv(f)
        else:
            data = pd.read_excel(f)
        return data


@login_required
def delete_file(request):
    fname = request.GET.get('fname')
    try:
        file = File.objects.get(fname=fname)
    except File.DoesNotExist:
        print('文件不存在')
    file.delete()
    return redirect('/table_basic')

