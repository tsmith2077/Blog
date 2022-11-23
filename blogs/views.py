from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """The home page for blogs."""
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted, create a new form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blog_id):
    """Edit an existing blog post."""
    blog = BlogPost.objects.get(id=blog_id)
    
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogForm(instance=blog)
    else:
        # POST data submitted; process data
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
        
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
