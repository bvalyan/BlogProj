from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from testApp.models import *
from django.shortcuts import render, get_object_or_404
from testApp.forms import PostForm;
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
   

     
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

def post_form_upload(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect(index)
    return render_to_response('blog/post_form_upload.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))

