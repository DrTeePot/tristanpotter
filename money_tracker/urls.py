from django.conf.urls import patterns, url
from money_tracker import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='money_index'),
                       )
