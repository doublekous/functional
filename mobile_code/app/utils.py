import http
import json
from io import StringIO
import random
import os
from urllib.error import URLError
from urllib.parse import urlencode

import celery
import requests
from django_redis import get_redis_connection


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    code = StringIO()
    for _ in range(length):
        code.write(str(random.randint(0, 9)))
    return code.getvalue()


SMS_SERVER = '106.ihuyi.com'
SMS_URL = '/webservice/sms.php?method=Submit'
SMS_ACCOUNT = 'C87871083'
SMS_PASSWORD = 'c88f63e58e1acfb1e5c42866c2a15bf6'
MSG_TEMPLATE = '您的验证码是：%s。请不要把验证码泄露给其他人。'

# 注册环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fangtx.settings')
# broker 代表消息代理（从哪里获取消息队列服务）
app = celery.Celery('common.utils', broker='redis://:1qaz2wsx@47.93.248.0:6379/0')
app.config_from_object('django.conf:settings')
# 用app.task装饰需要异步执行的函数（注册异步函数）
# 使用windows 10且使用celery4.x做开发需要先安装一个三方库
# pip install evnetlet
# celery -A common.utils worker -l info -P eventlet


@app.task
def send_sms_by_ihuyi(tel, code):
    """发送短信（调用互亿无线短信网关）"""
    params = urlencode({
        'account': SMS_ACCOUNT,
        'password': SMS_PASSWORD,
        'content': MSG_TEMPLATE % code,
        'mobile': tel,
        'format': 'json'
    })
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(SMS_SERVER, port=80, timeout=10)
    try:
        conn.request('POST', SMS_URL, params, headers)
        cli = get_redis_connection(alias='dejault')
        cli.set(f'mobile_code:{tel}', code, ex=120)
        return conn.getresponse().read().decode('utf-8')
    except URLError or KeyError as e:
        return json.dumps({
            'code': 500,
            'msg': '短信服务暂时无法使用'
        })
    finally:
        conn.close()


def send_sms_by_luosimao(tel, code):
    """发送短信验证码（调用螺丝帽短信网关）"""
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-524049379b633f7a4344494e95b09f89'),
        data={
            'mobile': tel,
            'message': f'您的验证码为{code}。【铁壳测试】'
        },
        timeout=10,
        verify=False)
    # return json.loads(resp.content)
    # Django 框架封装好的缓存调用方式（简单但是弱小）
    # caches['default'].set(f'mobile_code:{tel}', code, timeout=120)
    # 如果想使用原生的redis连接进行操作（强大）
    cli = get_redis_connection(alias='default')
    cli.set(f'mobile_code:{tel}', code, ex=120)
    return resp.content
