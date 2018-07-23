from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.appmain, name='appmain'),
    url(r'^syokyuu.html$', views.appmain2, name='appmain2'),
    url(r'^tyuukyuu.html$', views.appmain3, name='appmain3'),
    url(r'^zyoukyuu.html$', views.appmain4, name='appmain4'),
    url(r'^tyoukyuu.html$', views.appmain5, name='appmain5'),
    url('^$', views.kakikomi, name='kakikomi'),
]
