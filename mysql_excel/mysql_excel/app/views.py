from io import BytesIO
from urllib.parse import quote

import xlwt
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Emp, Dept


def get_style(*, color=0, bold=False, italic=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    # font.name = name
    font.colour_index = color
    font.bold = bold
    font.italic = italic
    style.font = font
    return style


PAGE_SIZE = 10


def export_emp_excel(request, page):
    # 创建excel工作薄
    workbook = xlwt.Workbook()
    # 向工作薄中添加工作表
    sheet = workbook.add_sheet('员工详细信息表')
    # 设置表头
    titles = ['编号', '姓名', '职位', '主管', '工资', '部门']
    # 插入表头
    for col, title in enumerate(titles):
        sheet.write(0, col, get_style(color=2, bold=True))
    # 可以通过only()或者defer()方法来进行SQL投影操作
    props = ('no', 'name', 'job', 'mgr', 'sal', 'dept')
    start, end = (page - 1) * PAGE_SIZE, page * PAGE_SIZE
    # 如果查询对象的同时还要查询它的关联对象 那么必须对自动生成的SQL语句进行优化
    # 否则将会引发1+N查询（也称为N+1查询，程序的性能会下降得非常明显而且数据库压力山大）
    # 如果有多对一关联，需要用连接查询加载关联对象那么可以用select_related()来加载
    # 如果有多对多关联，需要用连接查询加载关联对象那么可以用prefetch_related()来加载
    emps = Emp.objects.all().only(*props).select_related('dept'). \
               select_related('mgr').order_by('-sal')[start:end]
    # 通过数据库获得员工的数据填写在excel中
    for row, emp in enumerate(emps):
        for col, prop in enumerate(props):
            val = getattr(emp, prop, '')
            if isinstance(val, (Dept, Emp)):
                val = val.name
            sheet.write(row + 1, col, val)
        # 提取Excel表格的数据
        buffer = BytesIO()
        workbook.save(buffer)
        # 生成响应对象传输数据给浏览器
        resp = HttpResponse(buffer.getvalue(), content_type='application/msexcel')
        filename = quote('员工信息表.xls')
        resp['content-disposition'] = f'attachment; filename="{filename}"'
        return resp
