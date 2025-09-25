from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Payment, Product
from mongoengine import connect
import uuid
from datetime import datetime




# Connect to MongoDB
connect(
    db='mongo_db',
    username='admin',
    password='admin',
    host='mongodb://db_mongo:27017/',
    authentication_source='admin'  # important!
)









# ----------------- PostgreSQL -----------------
def create_user(request):
    username = request.GET.get('username', 'default_user')
    email = request.GET.get('email', 'user@example.com')

    user = User.objects.using('default').create(username=username, email=email)
    return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})


# ----------------- MongoDB -----------------
def create_product(request):
    name = request.GET.get('name', 'Sample Product')
    description = request.GET.get('description', '')
    price = float(request.GET.get('price', 0.0))

    product = Product(name=name, description=description, price=price)
    product.save()
    return JsonResponse({'name': product.name, 'price': product.price})


# ----------------- MySQL -----------------
def create_payment(request):
    user_id = int(request.GET.get('user_id', 1))
    product_id = request.GET.get('product_id', 'prod-1')
    amount = float(request.GET.get('amount', 100))
    status = request.GET.get('status', 'pending')

    payment = Payment.objects.using('mysql_db').create(
        user_id=user_id, product_id=product_id, amount=amount, status=status
    )
    return JsonResponse({'id': payment.id, 'status': payment.status, 'amount': payment.amount})

