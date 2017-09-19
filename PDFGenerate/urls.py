from django.conf.urls import url
from . import views

app_name='pdf'

urlpatterns = [
    url(r'^$', views.form.as_view(), name='form'),
    url(r'done$', views.view.as_view(), name='view'),
    url(r'admin$', views.admin.as_view(), name='admin'),
]