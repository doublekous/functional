from django.http import JsonResponse
from django.shortcuts import render

from app.utils import gen_mobile_code, send_sms_by_ihuyi


def mobile_code(request, tel):
    """短信验证码"""
    code = gen_mobile_code()
    request.session['mobile_code'] = code
    # 如果调用短信官网的函数返回字典对象就是JsonResponse进行处理
    # 如果返回的是字符串就用HttpResponse并且指定MIME类型即可
    # 调用三方平台的一个风险就是时间不可预估，但是我们的应用不能因为三方平台二阻塞
    # 所以调用三方平台不需要马上获得执行结果的场景都要异步化的处理
    # 让发送短信的函数延迟执行（将函数调用变成一条消息放到消息队列 - 消息的生产者）
    send_sms_by_ihuyi.delay(tel, code)
    return JsonResponse({'code': 20000, 'message': '消息已经发出'})