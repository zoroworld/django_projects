from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.create_user, name='create_user'),
    path('product/', views.create_product, name='create_product'),
    path('payment/', views.create_payment, name='create_payment'),
]
