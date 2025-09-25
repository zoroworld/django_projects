"""
URL configuration for caching project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # Redis
    path('set-redis/', views.set_redis_cache, name='set-redis'),
    path('display-redis/', views.display_redis_cache, name='display-redis'),

    # Memcached
    path('set-memcached/', views.set_memcached_cache, name='set-memcached'),
    path('display-memcached/', views.display_memcached_cache, name='display-memcached'),

    # File-based
    path('set-file/', views.set_file_cache, name='set-file'),
    path('display-file/', views.display_file_cache, name='display-file'),

    # Local memory
    path('set-local/', views.set_local_cache, name='set-local'),
    path('display-local/', views.display_local_cache, name='display-local'),
]

