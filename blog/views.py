from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})

def blog_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    # Use 'created_at' since 'published_date' does not exist
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})
