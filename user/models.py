from django.db import models
from django.shortcuts import HttpResponse
import re
import random
from DataFactory.settings import APIKEY
# from .models import VerifyCode
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    dept = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.CharField(max_length=64, unique=True)
    power = models.IntegerField(default=1)
    hirdate = models.DateField(auto_now_add=True)


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【**网】您的验证码是{code}。如非本人操作，请忽略本短信'.format(code=code)
        }

        # text必须要跟云片后台的模板内容 保持一致，不然发送不出去！
        # r = requests.post(self.single_send_url, data=parmas)
        # print(r)


# class ForCodeView(View):
#     """获取手机验证码"""
#     def post(self, request):
#         mobile = request.POST.get('mobile', '')
#         if mobile:
#             # 验证是否为有效手机号
#             mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
#             res = re.search(mobile_pat, mobile)
#             if res:
#                 # 生成手机验证码
#                 code = VerifyCode()
#                 code.mobile = mobile
#                 c = random.randint(1000, 9999)
#                 code.code = str(c)
#                 code.save()
#                 code = VerifyCode.objects.filter(mobile=mobile).first().code
#                 yunpian = YunPian(APIKEY)
#                 sms_status = yunpian.send_sms(code=code, mobile=mobile)
#                 msg = sms_status.msg
#                 return HttpResponse(msg)
#             else:
#                 msg = '请输入有效手机号码!'
#                 return HttpResponse(msg)
#         else:
#             msg = '手机号不能为空！'
#             return HttpResponse(msg)
