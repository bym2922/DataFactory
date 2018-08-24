import time
from django.utils.deprecation import MiddlewareMixin

import os


class AccessMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('***************')
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        with open(path+'\log.txt', 'a', encoding="utf-8") as f:
            try:
                username = request.session['username']
            except:
                username = '未登录用户'
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            option = request.get_full_path()
            print(option)

            # print(option.split('/')[1], option.split('/')[2].split('&')[0], option.split('/')[2].split('&')[1])
            f.write(username + ' ')
            f.write(date + ' ')
            f.write(option + '\n')
            print('*****************')
        return None

    def process_response(self, request, response):

        return response