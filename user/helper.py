from django.shortcuts import redirect


def login_required(view_func):
    def check(request):
        if request.session.get('uid'):
            return view_func(request)
        return redirect('/login')
    return check