# from typing_extensions import Required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PostForm
def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
            
            # No, Show Error 
     
    
    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    
    # Show
    return render(request, 'posts.html', 
                  {'posts': posts})

def delete(request, post_id):
    # Find post
    post = Post.objects.get(id= post_id)
    post.delete()
    return HttpResponseRedirect('/')