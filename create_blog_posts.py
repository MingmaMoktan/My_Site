import os
import django
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Import your models
from blog.models import Category, Post

# Create a category
cat, created = Category.objects.get_or_create(
    name='Data Engineering',
    slug='data-engineering'
)

# Create a blog post
post, created = Post.objects.get_or_create(
    title='Introduction to Data Engineering',
    slug='intro-to-data-engineering',
    category=cat,
    content='This is the content of the blog post.',
    published_date=timezone.now()
)

print("Blog post created:", post)
