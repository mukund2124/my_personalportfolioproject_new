from django.shortcuts import render
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.order_by('-date')[:4]
    return render(request, 'blog/all_blog.html', {'blogs':blogs})

