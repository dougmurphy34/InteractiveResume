__author__ = 'doug'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'resume.views.index', name='index'),
    url(r'joblist', 'resume.views.allmyjobs', name='joblist')
)
