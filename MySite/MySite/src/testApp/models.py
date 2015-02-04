from django.db import models
from django.contrib import admin
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
    
     

     
class Post(models.Model):
        title = models.CharField(max_length=255)
        slug = models.SlugField(unique=True, max_length=255)
        description = models.CharField(max_length=255)
        content = models.TextField()
        published = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
     
class Meta:
            ordering = ['-created']
     
def __unicode__(self):
            return u'%s' % self.title
     
def get_absolute_url(self):
            return reverse('testApp.views.post', args=[self.slug])
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)