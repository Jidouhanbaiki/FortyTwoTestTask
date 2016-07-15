from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^$', 'fortytwo_test_task.views.contacts', name=1'contacts'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
