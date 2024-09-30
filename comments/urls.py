from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentsList.as_view()),
    #path('collections/<int:pk>/', views.CommentDetail.as_view()),
]