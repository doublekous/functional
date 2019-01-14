"""中间件 - 拦截过滤器"""
import re

from django.http import JsonResponse
from django_redis import get_redis_connection

PATTERN = re.compile(r'/mobile_code/(?P<tel>1[3-9]\d{9})/')


def block_sms_middleware(get_resp):

    def middleware(request, *args, **kwargs):
        if request.path.startwith('/mobile_code'):
            matcher = PATTERN.fullmatch(request.path)
            if matcher:
                tel = matcher.group('tel')
                cli = get_redis_connection(alias='default')
                if cli.get(f'mobile_code:{tel}'):
                    resp = JsonResponse({'code': 20001, 'message': '请不要120秒之内重复发送'})
                else:
                    resp = get_resp(request, *args, **kwargs)
            else:
                resp = JsonResponse({'code': 20002, 'message': '请输入正确的手机号码'})
        else:
            get_resp(request, *args, **kwargs)
        return resp

    return middleware