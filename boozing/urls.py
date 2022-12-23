from django.urls import path
from . import views

urlpatterns = [
    path('drink/list', views.drink_list, name='drink_list'),
    path('drink/<int:pk>/', views.drink, name='drink'),
]