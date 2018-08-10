from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from math import ceil
from .forms import UserForm
from .models import User
from .helper import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect('/login', {'error': "用户不存在"})
        if check_password(password, user.password):
            request.session['uid'] = user.id
            request.session['username'] = user.username
            request.session['power'] = user.power
            return redirect('/index')
        else:
            return redirect('/login', {'error': '密码错误'})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            print('============')
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('/login')
        else:
            print(form.errors)
            return redirect('/register', {"error": form.errors})
    return render(request, 'register.html')


@login_required
def permission_assignment(request):
    page = int(request.GET.get('page', 1))  # 页码

    total = User.objects.count()  # 人员总数
    per_page = 15  # 每页人员数
    pages = ceil(total / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page

    user_list = User.objects.all().order_by('-id')[start:end]
    data = {
        'user_list': user_list,
        'pages': range(pages),
        'total': total
    }
    return render(request, 'permission_assignment.html', {'data': data})


@login_required
def logout(request):
    request.session.flush()
    return redirect('/index')


def page_recoverpw(request):

    return render(request, 'page_recoverpw.html')


@login_required
def change_pswd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        oldpswd = request.POST.get('password')
        newpswd = request.POST.get('password1')
        renewpswd = request.POST.get('password2')
        print(username, oldpswd, newpswd, renewpswd)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect('/change_pswd', {'error': "用户信息不存在"})
        if newpswd == renewpswd:
            if check_password(oldpswd, user.password):
                user.password = make_password(newpswd)
                user.save()
                # request.session.flush()
                print('密码已修改，请您重新登录！')
                return redirect('/logout', {'error': '密码已修改，请您重新登录！'})
            else:
                print('原密码输入错误')
                return redirect('/change_pswd', {'error': '原密码输入错误'})
        else:
            print('两次密码输入不一致！')
            return redirect('/change_pswd', {'error': '两次密码输入不一致！'})
    return render(request, 'change_pswd.html')


@login_required
def typography(request):
    uid = request.session.get('uid')
    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        return redirect('login')
    return render(request, 'typography.html', {'user': user})


@login_required
def user_manage(request):
    page = int(request.GET.get('page', 1))  # 页码

    total = User.objects.count()  # 人员总数
    per_page = 15  # 每页人员数
    pages = ceil(total / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page

    user_list = User.objects.all().order_by("power")[start:end]
    data = {
        'user_list': user_list,
        'pages': range(pages),
        'total': total
    }
    return render(request, 'user_manage.html', {'data': data})
