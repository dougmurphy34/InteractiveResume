__author__ = 'doug'

from django.conf.urls import patterns, include, url
from resume import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'joblist', views.all_my_jobs, name='job_list'),
    url(r'^job/(?P<job_id>\d+)/$', views.job_detail, name='job_detail'),
    url(r'^(?P<job_id>\d+)/$', views.job_detail),
)
