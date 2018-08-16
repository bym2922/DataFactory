from django.shortcuts import redirect
import http.client
import urllib
import random


def login_required(view_func):
    def check(request, *args):
        if request.session.get('uid'):
            return view_func(request, *args)
        return redirect('/login')
    return check



# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。
# （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；


host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account = "C48085107"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "b24e6054fe002577d26e3f15d9c06981"


def send_sms(text, mobile):
    params = urllib.parse.urlencode({
            'account': account,
            'password': password,
            'content': text,
            'mobile': mobile,
            'format': 'json',
        })
    headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
    }
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def randomforcode():
    forcode = random.randint(100000, 999999)
    print(forcode)
    return forcode

# if __name__ == '__main__':
    # mobile = "15718835208"
    # text = "您的验证码是："+randomforcode()+"。请不要把验证码泄露给其他人。(10分钟内有效)"
    # print(send_sms(text, mobile))
    # randomforcode()
