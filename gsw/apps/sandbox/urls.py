from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.app_list, name='app_list'),
    url(r'^projects/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
]
