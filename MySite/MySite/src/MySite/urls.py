from django.conf.urls import patterns, include, url
from django.contrib import admin
     
admin.autodiscover()

     
urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'testApp.views.index'),
        url(r'^(?P<slug>[\w\-]+)/$', 'testApp.views.post'),
        url(r"^add_comment/(\d+)/$", "add_comment"),
    )