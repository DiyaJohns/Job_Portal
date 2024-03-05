from django.db import models

# Create your models here.
class CompanyReg(models.Model):
    cname=models.CharField(max_length=80)
    clocation=models.CharField(max_length=40)
    ctype=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=17)
class UserReg(models.Model):
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    addrs=models.CharField(max_length=190)
    qual=models.CharField(max_length=90)
    email=models.EmailField()
    phno=models.CharField(max_length=12)
    uname=models.CharField(max_length=90)
    pswrd=models.CharField(max_length=29)
class AddVnc(models.Model):
    vno=models.IntegerField(max_length=20)
    vname=models.CharField(max_length=30)
    salary=models.IntegerField(max_length=10)
    nop=models.CharField(max_length=29)
    qual=models.CharField(max_length=30)
    compid=models.CharField(max_length=20)
    company=models.CharField(max_length=50)
    filled=models.IntegerField(default=0)
class ViewVnc(models.Model):
    applno=models.IntegerField(max_length=18)
    appdate=models.DateField(max_length=10)
    appid=models.IntegerField(max_length=4)
    appname=models.CharField(max_length=20)
    vno=models.IntegerField(max_length=10)
    job=models.CharField(max_length=10)
    cid=models.CharField(max_length=19)
    cname=models.CharField(max_length=50)
    status=models.CharField(max_length=15,default='New Application')




