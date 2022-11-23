"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home Page
    path('', views.index, name="index"),
    # Page for adding a new blog post.
    path('new_post/', views.new_post, name="new_post"),
    # Page for editing a blog post.
    path('edit_post/<int:blog_id>/', views.edit_post, name='edit_post'),
]
