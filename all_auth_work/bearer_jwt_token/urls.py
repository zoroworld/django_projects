from django.urls import path
from .views import protected_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/protected/', protected_view, name='protected_view'),

]
