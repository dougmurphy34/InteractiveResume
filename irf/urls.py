from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('resume.urls')),
    url(r'^contact/', 'resume.views.contact', name='contact'),
    url(r'^workshop/', 'irf.views.workshop', name='workshop'),
)
