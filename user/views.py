from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

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
            # 权限
        except User.DoesNotExist:
            print("用户不存在")
            return redirect('/login')
        if check_password(password, user.password):
            request.session['uid'] = user.id
            request.session['username'] = user.username
            request.session['power'] = user.power
            return redirect('/index')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return redirect('/register')
    return render(request, 'register.html')


@login_required
def permission_assignment(request):
    return render(request, 'permission_assignment.html')


@login_required
def logout(request):
    request.session.flush()
    return redirect('/index')


def page_recoverpw(request):
    return render(request, 'page_recoverpw.html')


@login_required
def typography(request):
    uid = request.session.get('uid')
    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        return redirect('login')
    return render(request, 'typography.html', {'user': user})
