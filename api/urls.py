from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardList, name="list"),
    path('detail/<str:pk>/', views.cardDetail, name="detail"),
    path('update/<str:pk>/', views.cardUpdate, name="update"),
    path('create/', views.cardCreate, name="create"),
    path('delete/<str:pk>/', views.cardDelete, name="delete"),
  ]