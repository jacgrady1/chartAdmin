from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gradeChartApp.views.home', name='home'),

    url(r'^blog/', include('blog.urls')),
    url(r'^$', 'gradeChartApp.views.home', name='home'),
    
)
