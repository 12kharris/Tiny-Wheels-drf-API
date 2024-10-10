from django.urls import path
from collection import views

urlpatterns = [
    path('collections/', views.CollecionsList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view()),
    path('collections/item/<int:pk>/', views.CollectionItemDetail.as_view()),
    path('collections/items/', views.CollectionItemList.as_view()),
]