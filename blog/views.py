from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    posts_list = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts_list})