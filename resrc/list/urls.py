# -*- coding: utf-8 -*-:
from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^(?P<list_pk>\d+)/$', views.single, name="list-single"),
    url(r'^(?P<list_pk>\d+)/(?P<list_slug>.+)/$',
        views.single, name="list-single-slug"),
    url(r'^a/(?P<link_pk>\d+)/$', views.ajax_own_lists, name="ajax-own-lists"),

    url(r'^add_default/$', views.ajax_add_to_default_list,
        name="ajax_add_to_default_list")
)
