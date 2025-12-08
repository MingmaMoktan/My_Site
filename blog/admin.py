from django.contrib import admin
from .models import Post, Category  # Import your models

# Register your models
admin.site.register(Post)
admin.site.register(Category)
