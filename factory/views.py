from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.core import serializers
from .forms import FileForm
from .models import File
from user.helper import login_required
import xlwt
import xlrd
import json
import time
import os
import pandas as pd
# Create your views here.


def index(request):
    fname = File.objects.get(fname='同仁堂.xlsx').fname
    # data = clear_data(fname)
    data = get_data(fname)
    return render(request, "index.html", {'data': data})


@login_required
def table_basic(request):
    file_list = File.objects.all()
    return render(request, "table_basic.html", {'file_list': file_list})


@login_required
def chart_columnar(request, fname):
    # data = clear_data(fname)
    data = get_data(fname)
    # return render(request, "chart_columnar.html", {'data': data})
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def chart_line(request, fname):
    # data = clear_data(fname)
    data = get_data(fname)
    print(type(data))
    # return render(request, "chart_line.html", {'data': data})
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')

@login_required
def chart_pie(request, fname):
    # data = clear_data(fname)
    data = get_data(fname)
    # return render(request, "chart_pie.html", {'data': data})
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def chart_scatter(request, fname):
    # data = clear_data(fname)
    data = get_data(fname)
    # return render(request, "chart_scatter.html", {'data': data})
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def table_cmplete(request, fname):
    request.session['fname'] = fname
    # data = get_data(fname)
    data = clear_data(fname)
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
                    return redirect('/table_basic')
                else:
                    print("文件类型不支持！")
                return render(request, "file_upload.html")
        else:
            return render(request, "file_upload.html")
    else:
        return render(request, "file_upload.html")


# 读取表格数据, 按行获取
def get_data(fname):
    f = File.objects.get(fname=fname).fpath
    if f:
        # data = pd.read_excel(f)
        data = xlrd.open_workbook(f, formatting_info=True)
        tblTDLYMJANQSXZB = data.sheets()[0]
        # 找到有几列几列
        nrows = tblTDLYMJANQSXZB.nrows  # 行数
        ncols = tblTDLYMJANQSXZB.ncols  # 列数
        print(nrows, ncols)
        totalArray = []
        arr = []
        for i in range(0, ncols):
            arr.append(tblTDLYMJANQSXZB.cell(0, i).value)
        for rowindex in range(1, nrows):
            dic = {}
            for colindex in range(0, ncols):
                s = tblTDLYMJANQSXZB.cell(rowindex, colindex).value
                dic[arr[colindex]] = s
            totalArray.append(dic)
        # a = json.dumps(totalArray, ensure_ascii=False)
        # print(a)
        print(totalArray)
    return totalArray


# 对读取到的数据进行处理，为json格式
def clear_data(fname):
    f = File.objects.get(fname=fname).fpath
    if f:
        data = pd.read_excel(f)
#     data = get_data(fname)
#     data1 = dict()
#     for i in range(len(data.columns)):
#         data1.update({data.columns[i]: data[data.columns[i]].values.tolist()})
#     print(type(data1))
#     # return HttpResponse(json.dumps(data1), content_type='application/json')
#     print(data1)
        return data