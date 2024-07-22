from django.shortcuts import render
from django.http import HttpResponse
from.models import *
# Create your views here.

def Index(request):
    #updated post display first, maximum 2 post display here 
    all_posts = Blog.objects.all().order_by('-id')[:2] 
    #display only 2 tag for home page
    all_tags = Tag.objects.all()[:2]

    params = {'all_posts': all_posts, 'all_tags': all_tags}
    return render(request, 'arpan/index.html', params)


def ProjectDetails(request):
    return render(request, 'arpan/project-details.html')


def BlogDetails(request, slug):
    blog = Blog.objects.get(slug=slug)
    recent_posts = Blog.objects.all().order_by('-id')[:2]
    # Get all blogs ordered by their creation date
    all_blogs = Blog.objects.order_by('created_at')
    blog_index = list(all_blogs).index(blog)
    # Determine previous and next blogs
    prev_blog = all_blogs[blog_index - 1] if blog_index > 0 else None
    next_blog = all_blogs[blog_index + 1] if blog_index < len(all_blogs) - 1 else None

    params = {'blog': blog, 'prev_blog': prev_blog, 'next_blog': next_blog, 'recent_posts': recent_posts}
    return render(request, 'arpan/blog-details.html', params)