from django.urls import path
from collection import views

urlpatterns = [
    path('collections/', views.CollecionsList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view()),
]