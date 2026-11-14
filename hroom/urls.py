from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('catalog/', include('menu.urls')),
    path('register/', menu_views.register_view, name='register'),
    path('login/', menu_views.login_view, name='login'),
    path('logout/', menu_views.logout_view, name='logout'), 
    path('profile/', TemplateView.as_view(template_name='pages/profile.html'), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)