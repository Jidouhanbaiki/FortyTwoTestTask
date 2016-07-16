from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'contacts.views.index', name='index'),
    (r'^requests/$', TemplateView.as_view(template_name='requests.html')),
    url(r'^admin/', include(admin.site.urls)),
)
