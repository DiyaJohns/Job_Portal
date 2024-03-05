from django.contrib import admin
from myapp.models import CompanyReg
from myapp.models import UserReg,AddVnc,ViewVnc
# Register your models here.


admin.site.register(CompanyReg)
admin.site.register(UserReg)
admin.site.register(AddVnc)
