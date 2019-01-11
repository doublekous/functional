from django.db import models

# Create your models here.
from django.db import models


class Dept(models.Model):
    no = models.IntegerField(primary_key=True, db_column='dno')
    name = models.CharField(max_length=10, db_column='dname')
    loc = models.CharField(max_length=20, db_column='dloc')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        app_label = 'hrs'
        db_table = 'tb_dept'


class Emp(models.Model):
    no = models.IntegerField(primary_key=True, db_column='eno')
    name = models.CharField(max_length=20, db_column='ename')
    job = models.CharField(max_length=20)
    mgr = models.ForeignKey('self', models.PROTECT, db_column='mgr', blank=True, null=True)
    sal = models.IntegerField()
    comm = models.IntegerField(blank=True, null=True)
    dept = models.ForeignKey(Dept, models.DO_NOTHING, db_column='dno', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        app_label = 'hrs'
        db_table = 'tb_emp'