from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'contacts.views.index', name='index'),
    url(r'^requests/$', 'contacts.views.request_logs', name='request_logs'),
    url(r'^admin/', include(admin.site.urls)),
)
