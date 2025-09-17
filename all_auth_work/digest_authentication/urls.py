from django.urls import path
from .views import SecretView, get_auth

urlpatterns = [
    path("secret/", SecretView.as_view(), name="secret"),
    path("getkey/", get_auth, name="get-nonce"),
]
