from django.urls import path
from brands import views

urlpatterns = [
    path('brands/', views.BrandsList.as_view()),
    path('series/', views.SeriesList.as_view()),
]
