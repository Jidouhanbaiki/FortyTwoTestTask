from django.conf.urls import patterns, include, url

from apps.contacts.views import ContactDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^people/(?P<pk>[0-9]+)/$',
        ContactDetailView.as_view(),
        name='contacts'
        ),
    url(r'^$', 'contacts.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
