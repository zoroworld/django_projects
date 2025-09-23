from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import OTP
from django.utils import timezone
from datetime import timedelta
from .models import MobileOTP
from .utils import send_otp_sms
from django.contrib.auth import login


def send_otp_email(user):
    otp = OTP(user=user)
    code = otp.generate_otp()
    send_mail(
        'Your OTP Code',
        f'Your OTP is {code}. It is valid for 5 minutes.',
        'from@example.com',
        [user.email],
    )

# def login_view(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         try:
#             user = User.objects.get(email=email)
#             send_otp_email(user)
#             request.session['user_id'] = user.id
#             return redirect('verify_otp')
#         except User.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Email not found'})
#     return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        user, created = User.objects.get_or_create(
            email=email,
            defaults={"username": email.split("@")[0]}  # simple username
        )
        send_otp_email(user)
        request.session['user_id'] = user.id
        return redirect('verify_otp')
    return render(request, 'login.html')


def verify_otp_view(request):

    if request.method == "POST":
        user_id = request.session.get('user_id')
        print(f" get: {user_id }")
        code = request.POST['otp']
        user = User.objects.get(id=user_id)
        otp_obj = OTP.objects.filter(user=user, code=code).first()
        if otp_obj and (timezone.now() - otp_obj.created_at) < timedelta(minutes=5):
            # OTP is valid
            del request.session['user_id']
            # Log the user in (optional: create a session)
            return render(request, 'success.html', {'user': user})
        else:
            return render(request, 'verify_otp.html', {'error': 'Invalid or expired OTP'})
    return render(request, 'verify_otp.html')



#mail

def login_with_phone(request):
    if request.method == "POST":
        phone = request.POST['phone']
        user, created = User.objects.get_or_create(
            username=phone,  # use phone as username
            defaults={"email": ""}
        )
        otp_obj = MobileOTP.objects.create(user=user, phone_number=phone)
        otp = otp_obj.generate_otp()
        send_otp_sms(phone, otp)
        request.session['user_id'] = user.id
        return redirect('verify_mobile_otp')
    return render(request, 'login_with_phone.html')


def verify_mobile_otp(request):
    if request.method == "POST":
        otp = request.POST['otp']
        user_id = request.session.get('user_id')

        if not user_id:
            return redirect('login_with_phone')  # session expired

        user = User.objects.get(id=user_id)
        otp_obj = MobileOTP.objects.filter(user=user).order_by('-created_at').first()

        if otp_obj and str(otp_obj.code) == str(otp) and (timezone.now() - otp_obj.created_at) < timedelta(minutes=5):
            # OTP valid → log user in explicitly with backend
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            del request.session['user_id']
            return render(request, 'success.html', {"user": user})
        else:
            return render(request, 'verify_mobile_otp.html', {"error": "Invalid or expired OTP"})

    return render(request, 'verify_mobile_otp.html')
