"""
工具函数
"""
import random

from io import StringIO


def get_ip_address(request):
    """获得请求的IP地址"""
    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    return ip or request.META['REMOTE_ADDR']


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    code = StringIO()
    for _ in range(length):
        code.write(str(random.randint(0, 9)))
    return code.getvalue()


ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def gen_captcha_text(length=4):
    """生成指定长度的图片验证码文字"""
    code = StringIO()
    chars_len = len(ALL_CHARS)
    for _ in range(length):
        index = random.randrange(chars_len)
        code.write(ALL_CHARS[index])
    return code.getvalue()
