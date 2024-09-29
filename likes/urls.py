from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeDislikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDislikeDetail.as_view()),
]