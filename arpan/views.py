from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return render(request, 'arpan/index.html')

def ProjectDetails(request):
    return render(request, 'arpan/project-details.html')