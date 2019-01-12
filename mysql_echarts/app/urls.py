from django.urls import path

from app.views import mysql_echarts

urlpatterns = [
    path('mysql_echarts/', mysql_echarts),
]