from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('order/', views.make_order, name='make_order'),
    path('favorite/<int:order_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
]