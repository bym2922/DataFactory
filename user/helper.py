from django.shortcuts import redirect


def login_required(view_func):
    def check(request, *args):
        if request.session.get('uid'):
            return view_func(request, *args)
        return redirect('/login')
    return check