from django.urls import path
from .views import MyProtectedView, APIKeyViewSet

urlpatterns = [
    path('data/', MyProtectedView.as_view(), name='hello'),
    path('key/', APIKeyViewSet.as_view(), name='key'),
]


# curl -H "Authorization: Api-Key your-api-key" http://localhost:8000/key/
