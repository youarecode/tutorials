from django.shortcuts import render
from .models import Post, Category
# Create your views here.

def blog(request):

    posts    = Post.objects.all()
    category = Category.objects.all()
    return render(request, 'blog.html', {'posts':posts, 'category':category})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category.html', {'category':category, 'posts':posts})