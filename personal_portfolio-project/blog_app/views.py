from django.shortcuts import render
from .models import Blog
# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:10]  # most recent 10 blogs
    no_blogs = len(blogs)
    return render(request, 'blog/all_blogs.html', {
        'no_blogs': no_blogs,
        'blogs': blogs,
    })
