from django.contrib import admin
from django.urls import path, include  # обязательно include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ← ЭТО добавляет маршруты из приложения main
]