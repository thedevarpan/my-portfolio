from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from myblog.models import Blog, Tag, Author, BlogCategory



# Create your views here.
def Index(request):
    all_posts = Blog.objects.all().order_by('-id')[:2] 
    all_tags = Tag.objects.all()
    print(all_posts)
    params = {'all_posts': all_posts, 'all_tags': all_tags}
    return render(request, 'arpan/index.html', params)


def ProjectDetails(request):
    return render(request, 'arpan/project-details.html')


