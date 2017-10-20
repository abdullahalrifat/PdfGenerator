from django.conf.urls import url
from . import views

app_name='pdf'

urlpatterns = [
    url(r'^$', views.forms, name='form'),
    url(r'done$', views.view.as_view(), name='view'),
    url(r'admin$', views.admin.as_view(), name='admin'),
    url(r'gen$', views.gen.as_view(), name='gen'),
]