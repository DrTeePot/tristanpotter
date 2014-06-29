from django.conf.urls import patterns, url

from production.personal import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='personal_index'),
                       url(r'involvements/', views.index, name='personal_involvements'),
                       url(r'projects/', views.index, name='personal_projects'),
                       )
