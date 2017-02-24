# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from VertiNeuch.urls import urlpatterns as VertiNeuch_urls

urlpatterns = [
    url(r'^', include(VertiNeuch_urls, namespace='VertiNeuch')),
]
