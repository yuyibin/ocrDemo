from django.urls import path

from . import views

from django.conf.urls import url

urlpatterns = [
    #path('', views.index, name='demo'),
    path('', views.Upload),
    path("upload", views.Upload),
    url(r'^upload', views.Upload),  # 配置当访问index/时去调用views下的index方法

]