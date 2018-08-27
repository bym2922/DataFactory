from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from math import ceil
from .forms import UserForm
from .models import User
from .helper import login_required, randomforcode, send_sms

# Create your views here.

FORCODE = ''


def login(request):
    if request.method == 'POST':
        phone = request.POST.get('username')
        password = request.POST.get('password')
        print(phone, password)
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return redirect('/login', {'error': "用户不存在"})
        if check_password(password, user.password):
            print(user.phone)
            request.session['uid'] = user.id
            request.session['phone'] = user.phone
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

    user_list = User.objects.all().order_by('-power')[start:end]
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        forcode = request.POST.get('forcode')
        print(password, password2, phone)
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            print("用户不存在！")
        if username and password and password == password2:
            if int(forcode) == int(FORCODE):
                user.password = make_password(password)
                user.save()
                print('密码已重置！')
                redirect('/logout')
            else:
                print('验证码输入错误！')
                redirect('/page_recoverpw')
        else:
            print("两次密码输入不一致！")
            redirect('/page_recoverpw')
    return render(request, 'page_recoverpw.html')


def send_forcode(request):
    if request.method == 'POST':
        CODE = randomforcode()
        global FORCODE
        FORCODE = FORCODE + str(CODE)
        phone = request.POST.get('mobile')
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            print("用户不存在！")
        text = "您的验证码是：" + FORCODE + "。请不要把验证码泄露给其他人。"
        send_sms(text, phone)
        print(text)
        return HttpResponse(text)


@login_required
def change_pswd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        oldpswd = request.POST.get('password')
        newpswd = request.POST.get('password1')
        renewpswd = request.POST.get('password2')
        print(username, oldpswd, newpswd, renewpswd)
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return redirect('/change_pswd', {'error': "用户信息不存在"})
        if newpswd == renewpswd:
            if check_password(oldpswd, user.password):
                user.password = make_password(newpswd)
                user.save()
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

    user_list = User.objects.all().order_by("-hirdate")[start:end]
    data = {
        'user_list': user_list,
        'pages': range(pages),
        'total': total
    }
    return render(request, 'user_manage.html', {'data': data})


@login_required
def delete_user(request):
    phone = request.GET.get('phone')
    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        print('用户不存在！')
    user.delete()

    print('删除成功！')
    return user_manage(request)


@login_required
def update_user(request):
    phone = request.GET.get('phone')
    print('****')
    print(phone)

    power = request.GET.get('power')
    print(power)
    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        print('用户不存在！')
    user.power = power
    user.save()
    return permission_assignment(request)

