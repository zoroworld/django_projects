from django.db import models
from django.contrib.auth.models import User
import random

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()
        return self.code



class MobileOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()
        return self.code
