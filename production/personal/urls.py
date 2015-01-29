from django.conf.urls import patterns, url

from production.personal import views


urlpatterns = patterns('',  # TODO edit the license at the top of files
                       url(r'^$', views.index, name='personal_index'),
                       url(r'involvements/', views.involvements, name='personal_involvements'),
                       url(r'projects/', views.projects, name='personal_projects'),
                       url(r'about/', views.about, name='personal_about')  # TODO Add this
                       )
