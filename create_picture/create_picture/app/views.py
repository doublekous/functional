import os

from urllib.parse import quote
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render

# Create your views here.
from app.captcha import Captcha
from app.utils import gen_captcha_text


def captcha(request):
    code_text = gen_captcha_text()
    code_bytes = Captcha.instance().generate(code_text)
    return HttpResponse(code_bytes, content_type='image/png')


def download(request):
    path = os.path.dirname(__file__)
    # 如果要动态生成PDF报表可以使用ReportLab三方库
    file_stream = open(f'{path}/resources/Git工作流程.pdf', 'rb')
    file_iter = iter(lambda: file_stream.read(4096), b'')
    resp = StreamingHttpResponse(file_iter, content_type='application/pdf')
    # resp['content-type'] = 'application/pdf'
    filename = quote('Git工作流程.pdf')
    # inline - 内联打开 / attachment - 附件下载
    resp['content-disposition'] = f'attachment; filename="{filename}"'
    return resp