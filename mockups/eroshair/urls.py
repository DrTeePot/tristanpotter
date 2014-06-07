from django.conf.urls import patterns, url
from mockups.eroshair import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='eros_index'),
                       )
