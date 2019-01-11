from django.urls import path

from app.views import export_emp_excel

urlpatterns = [
    path('excel/<int:page>/', export_emp_excel),
]