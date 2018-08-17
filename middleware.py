import time
from django.utils.deprecation import MiddlewareMixin


class AccessMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('***************')
        with open('files\log.txt', 'a', encoding="utf-8") as f:
            try:
                username = request.session['username']
            except:
                username = '未登录用户'
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            option = request.get_full_path()
            f.write(username + ' ')
            f.write(date + ' ')
            f.write(option + '\n')

        return None

    def process_response(self, request, response):
        return response