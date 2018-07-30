from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.core import serializers
from .forms import FileForm
from .models import File
from user.helper import login_required
import xlwt
import json
import time
import os
import pandas as pd
# Create your views here.

fpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    # clear_data(request)
    return render(request, "index.html")


@login_required
def table_basic(request):
    file_list = File.objects.all()
    return render(request, "table_basic.html", {'file_list': file_list})


@login_required
def chart_columnar(request):
    uname = request.session.get('username')
    data = clear_data(uname)
    return render(request, "chart_columnar.html", {'data': data})


@login_required
def chart_line(request):
    uname = request.session.get('username')
    data = clear_data(uname)
    return render(request, "chart_line.html", {'data': data})


@login_required
def chart_pie(request):
    uname = request.session.get('username')
    data = clear_data(uname)
    return render(request, "chart_pie.html", {'data': data})


@login_required
def chart_scatter(request):
    uname = request.session.get('username')
    data = clear_data(uname)
    return render(request, "chart_scatter.html", {'data': data})


@login_required
def table_cmplete(request):
    uname = request.session.get('username')
    data = get_data(uname)
    a = data.index.tolist()
    b = []
    data1 = dict()
    for i in a:
        b.append(data.iloc[i].values.tolist())
    for i, j in zip(a, b):
        data1.update({str(i): j})
    data2 = {'xxx': data.columns.tolist()}
    return render(request, "table_complete.html", {'data': data1, 'data2': data2})


@login_required
def file_upload(request):
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
            # filename = fname.split(".")[0]
            fileext = fname.split(".")[1]
            with open(os.path.join('files', fname), 'w', encoding="utf-8") as f:
                if fileext == "xlsx" or fileext == "xls" or fileext == "csv":
                    data = pd.read_excel(file)
                    data1 = list(pd.read_excel(file))
                    # 创建一个workbook 设置编码
                    workbook = xlwt.Workbook(encoding='utf-8')
                    # 创建一个worksheet
                    worksheet = workbook.add_sheet('My Worksheet')
                    for i in range(len(data1)):
                        worksheet.write(0, i, str(data1[i]))
                        d1 = data[data1[i]]
                        for j in range(len(d1)):
                            if str(d1[j]) == 'nan':
                                d1[j] = ''
                            # 写入excel 参数对应 行, 列, 值
                            worksheet.write(j+1, i, str(d1[j]))
                            # 保存到本地
                            workbook.save('files/'+fname)
                    date = time.localtime(time.time())
                    date = time.strftime('%Y-%m-%d %H:%M:%S', date)
                    f2 = File(fname=fname, fpath=fpath+'\\files\\'+fname, uname=uname, date=date)
                    # 将本地文件保存到数据库
                    f2.save()
                    # request.session['fid'] = f2.id
                    # request.session['fname'] = f2.fname
                    print(f2.fname, f2.date, f2.fpath, f2.uname)
                    file_list = File.objects.all()
                    for i in file_list:
                        print(i.fname, i.uname, i.fpath, i.date)
                    return redirect('/table_basic')
                else:
                    print("文件类型不支持！")
                    # for line in file:
                    #     print(line)
                    #     line1 = line.decode("utf-8")
                    #     f.write(line1)
                return render(request, "file_upload.html")
        else:
            return render(request, "file_upload.html")
    else:
        return render(request, "file_upload.html")


# @login_required
def get_data(uname):
    f = File.objects.get(uname=uname).first()
    print(f)
    data = pd.read_excel(fpath + '\\files\\' + fname)
    print(data)
    return data


# @login_required
def clear_data(uname):
    data = get_data(uname)
    data1 = dict()
    for i in range(len(data.columns)):
        data1.update({data.columns[i]: data[data.columns[i]].values.tolist()})
    print(type(data1))
    # len1 = data.count().max()
    # return HttpResponse(json.dumps(data1), content_type='application/json')
    return data1