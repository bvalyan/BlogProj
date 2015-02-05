from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

     
admin.autodiscover()

     
urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', 'testApp.views.index'),
        url(r'^(?P<slug>[\w\-]+)/$', 'testApp.views.post'),
        url(r"^add_comment/(\d+)/$", "add_comment"),
        url(r'^comments/', include('django.contrib.comments.urls')),
        url(r'^post/form_upload.html$',
        'testApp.views.post_form_upload', name='post_form_upload'),)
        
urlpatterns += staticfiles_urlpatterns()