from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from testApp.models import *
from django.shortcuts import render, get_object_or_404
   

     
def index(request):
        # get the blog posts that are published
        posts = Post.objects.filter(published=True)
        # now return the rendered template
        return render(request, 'blog/index.html', {'posts': posts})
     
def post(request, slug):
        # get the Post object
        post = get_object_or_404(Post, slug=slug)
        # now return the rendered template
        return render(request, 'blog/post.html', {'post': post})