from django.urls import path
from .views import login_view, verify_otp_view, login_with_phone, verify_mobile_otp


urlpatterns = [
    path('login/', login_view, name='login'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    path('login-phone/', login_with_phone, name='login_with_phone'),
    path('verify-mobile-otp/', verify_mobile_otp, name='verify_mobile_otp'),
]

