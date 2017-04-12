# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.LessonListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^new/$',
        view=views.LessonCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.LessonDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.LessonUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>\d+)/delete/$',
        view=views.LessonDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'^(?P<pk>\d+)/subscribe/$',
        view=views.LessonSubscribeView.as_view(),
        name='subscribe'
    ),
]
