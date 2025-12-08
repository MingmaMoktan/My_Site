from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog_list'),
    path('<int:pk>/', views.post_details, name='post_details'),
    path('category/<slug:category_slug>/', views.blog_category, name='blog_category'),
]
