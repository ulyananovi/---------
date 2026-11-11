from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('catalog/', TemplateView.as_view(template_name='pages/catalog.html'), name='catalog'),
    path('register/', TemplateView.as_view(template_name='pages/register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='pages/login.html'), name='login'),
    path('profile/', TemplateView.as_view(template_name='pages/profile.html'), name='profile'),
]