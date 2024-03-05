from django.urls import path
from.import views
urlpatterns=[
    path('',views.index),
    path('reg/',views.reg),
    path('ureg/',views.userreg),
    path('lgs/',views.login),
    path('advnc/',views.addvacancy),
    path('vy/',views.viewvacancy),
]