from django.urls import path
from . import views

urlpatterns = [
    path('drink/list', views.drink_list, name='drink_list'),
    path('drink/<int:pk>/', views.drink, name='drink'),

    path('drink/create', views.create_drink, name='create_drink'),
    path('drink_type/', views.DrinkTypeTView.as_view(), name='drink_type_list'),
    
    path('test', views.test)
]