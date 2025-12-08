from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField  # Import CKEditor field

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Optional: URL for category pages
        return reverse('category_posts', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()  # <-- CKEditor rich text field
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ['-created_at']  # Default ordering by newest first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # URL for individual posts using the slug
        return reverse('post_details', args=[self.slug])
