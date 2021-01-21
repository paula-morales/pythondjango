from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('card-list/', views.cardList, name="card-list"),
    path('card-detail/<str:pk>/', views.cardDetail, name="card-Detail"),
    path('card-update/<str:pk>/', views.cardUpdate, name="card-update"),
    path('card-create/', views.cardCreate, name="card-Create"),
    path('card-delete/<str:pk>/', views.cardDelete, name="card-Delete"),
  ]