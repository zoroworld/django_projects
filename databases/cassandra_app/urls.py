from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.create_feedback, name='create_feedback'),
]