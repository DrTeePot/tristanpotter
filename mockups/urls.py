from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^eros/', include('mockups.eroshair.urls'), name='eros'),
                       )
