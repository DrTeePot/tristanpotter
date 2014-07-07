from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tristanpotter.views.personal', name='personal'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('production.personal.urls')),
    url(r'^tristan$', lambda x: HttpResponseRedirect('/tristan/')),
    url(r'^tristan/', include('production.personal.urls'), name='personal'),
    url(r'^money/', include('money_tracker.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
