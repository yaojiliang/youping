from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^check_is_num/$', views.check_is_num),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^detail/$', views.detail),
    url(r'^add_shoppingcar/$', views.add_shoppingcar),
    url(r'^phone/', views.phone),
    url(r'^pad/', views.pad),
    url(r'^computer/', views.computer),
]