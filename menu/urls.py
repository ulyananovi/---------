from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('add/', views.add_dish, name='add_dish'),
    path('edit/<int:pk>/', views.edit_dish, name='edit_dish'),
    path('delete/<int:pk>/', views.delete_dish, name='delete_dish'),
]