from django.urls import path
from .views import token_login, protected_view

urlpatterns = [
    path("api/token/", token_login, name="token_login"),
    path("api/protected/", protected_view, name="protected_view"),
]
