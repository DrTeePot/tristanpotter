from django.conf.urls import patterns, url

from production.personal.home import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='home_index'),
                       url(r'involvements/', views.index, name='home_involvements'),
                       url(r'projects/', views.index, name='home_projects'),
                       )
