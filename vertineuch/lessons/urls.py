from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.courList.as_view(), name='list'),
    url(r'^new/$', views.courCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.courDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.courUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.courDelete.as_view(), name='delete'),
]
