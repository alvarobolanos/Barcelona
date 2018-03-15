from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employee/([a-z0-9-]+)/$', views.detail, name='detail'),
    url(r'^employee/([a-z0-9-]+)/edit/$', views.edit, name='edit'),
]