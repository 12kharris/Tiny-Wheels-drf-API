from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path("posts/liked/", views.LikedPostList.as_view()),
    path("tags/", views.TagList.as_view()),
]