from django.conf.urls import patterns, url

from personal.home import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='home_index'),
                       )
