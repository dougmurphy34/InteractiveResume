from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # TODO 2): If contact doesn't belong in resume, then I need a new views.py page for irf.

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('resume.urls')),
    url(r'^contact/', 'resume.views.contact', name='contact'),
)
