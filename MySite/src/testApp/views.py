from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from testApp.models import *
from django.shortcuts import render, get_object_or_404
from testApp.forms import PostForm;
from django.http import HttpResponseRedirect, HttpResponse

   

     
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
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            content = form.cleaned_data['content']
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id': post.id}))
 
    return render(request, 'blog/post_form_upload.html', {
        'form': form,
    })
    
    def id_form_upload(request):
      if request.method == 'GET':
          form = PostForm()
      else:
          # A POST request: Handle Form Upload
          form = PostForm(request.POST) # Bind data from request.POST into a PostForm
   
          # If data is valid, proceeds to create a new post and redirect the user
          if form.is_valid():
              content = form.cleaned_data['content']
              return HttpResponseRedirect(reverse('post_detail',
                                                  kwargs={'post_id': post.id}))
   
      return render(request, 'blog/id_form_upload.html', {
          'form': form,
      })