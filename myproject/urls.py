from django.contrib import admin  # Importación que falta
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta al panel de administración
    path('', auth_views.LoginView.as_view(), name='login'),  # Redirigir a login como página principal
    path('myapp/', include('myapp.urls')),  # Aquí 'myapp' es tu aplicación principal
]
