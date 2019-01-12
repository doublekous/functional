from django.db import connections
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def mysql_echarts(request):
    names, totals = [], []
    # 通过django封装的connections来获取数据库连接
    # 然后创建游标方式来发出原生sql语句实现crud操作（性能更好）
    with connections['default'].cursor() as cursor:
        cursor.execute('select name, total from '
                       ' (select agentid, count(agentid) as total '
                       ' from tb_agent_estate group by agentid) t1 '
                       ' inner join tb_agent t2 on t1.agentid=t2.agentid')
        for row in cursor.fetchall():
            names.append(row[0])
            totals.append(row[1])
        return JsonResponse({'names': names, 'totals': totals})


def home(request):
    return render(request, 'index.html')