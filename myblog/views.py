from django.shortcuts import render, redirect, get_object_or_404
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



# def AddComment(request):
#     try:
#         if request.method == 'POST':
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             message =request.POST.get('message')            
#             post_slug = request.POST.get('post_slug')
#             blog_post = get_object_or_404(Blog, slug=post_slug)

#             Comment.objects.create(
#                 post=blog_post,
#                 # user=request.user,
#                 user_name=name,
#                 email=email,
#                 message=message
#             )
#             return redirect('BlogDetails', slug=post_slug)             
 
#     except Exception as e:
#         print(e)
#     return HttpResponse ("This is home page")


def AddComment(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            post_slug = request.POST.get('post_slug')
            parent_id = request.POST.get('parent_id')
            blog_post = get_object_or_404(Blog, slug=post_slug)

            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)

            Comment.objects.create(
                post=blog_post,
                user_name=name,
                email=email,
                message=message,
                parent_comment=parent_comment
            )
            return redirect('BlogDetails', slug=post_slug)
 
    except Exception as e:
        print(e)
    return HttpResponse("This is home page")