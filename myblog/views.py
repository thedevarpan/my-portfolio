from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from.models import *
# Create your views here.

def BlogPost(request):
    all_blogs = Blog.objects.all().order_by('-id')
    params = {'all_blogs':all_blogs}
    return render(request, 'myblog/blog-classic.html', params)



def BlogDetails(request, slug):
    blog = Blog.objects.get(slug=slug)

    recent_posts = Blog.objects.all().order_by('-id')[:2]
    # Get all blogs ordered by their creation date
    all_blogs = Blog.objects.order_by('created_at')
    blog_index = list(all_blogs).index(blog)
    # Determine previous and next blogs
    prev_blog = all_blogs[blog_index - 1] if blog_index > 0 else None
    next_blog = all_blogs[blog_index + 1] if blog_index < len(all_blogs) - 1 else None

    #add blog comments

    params = {'blog': blog, 'prev_blog': prev_blog, 'next_blog': next_blog, 'recent_posts': recent_posts}
    return render(request, 'myblog/blog-details.html', params)


# def BlogDetails(request, slug):
#     blog = Blog.objects.get(slug=slug)

#     recent_posts = Blog.objects.all().order_by('-id')[:2]
#     # Get all blogs ordered by their creation date
#     all_blogs = Blog.objects.order_by('created_at')
#     blog_index = list(all_blogs).index(blog)
#     # Determine previous and next blogs
#     prev_blog = all_blogs[blog_index - 1] if blog_index > 0 else None
#     next_blog = all_blogs[blog_index + 1] if blog_index < len(all_blogs) - 1 else None

#     #add blog comments

#     params = {'blog': blog, 'prev_blog': prev_blog, 'next_blog': next_blog, 'recent_posts': recent_posts}
    
#     return render(request, 'myblog/blog-details.html', params)


def AddComment(request):
    return HttpResponse ("This is home page")