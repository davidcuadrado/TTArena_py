from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts_list = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts_list})

def category(request, category_id):
    category_retrieved = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category_retrieved})
