# # my models
# # app/models.py
# from django.db import models
# from mongoengine import Document, StringField, FloatField, DateTimeField
# import datetime
#
# # -------------------------
# # PostgreSQL -> User model
# # -------------------------
# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = "users"
#         app_label = "postgres_app"
#
#
# # -------------------------
# # MongoDB -> Product model
# # -------------------------
#
# class Product(Document):
#     name = StringField(max_length=200, required=True)
#     description = StringField()
#     price = FloatField(required=True)
#     created_at = DateTimeField(default=datetime.datetime.utcnow)
#
#     meta = {
#         "collection": "products"
#     }
#
#
#
# # -------------------------
# # MySQL -> Payment model
# # -------------------------
# class Payment(models.Model):
#     user_id = models.IntegerField()  # reference User (manual FK because diff DB)
#     product_id = models.CharField(max_length=100)  # reference Product
#     amount = models.FloatField()
#     status = models.CharField(max_length=50, choices=[
#         ("pending", "Pending"),
#         ("completed", "Completed"),
#         ("failed", "Failed"),
#     ])
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = "payments"
#         app_label = "mysql_app"
#
#
# # -------------------------
# # Cassandra -> Feedback model
# # -------------------------
# from django_cassandra_engine.models import DjangoCassandraModel
# from cassandra.cqlengine import columns
# import uuid
# from datetime import datetime
#
# class Feedback(DjangoCassandraModel):
#     feedback_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     user_id = columns.Integer()
#     product_id = columns.Text()
#     comment = columns.Text()
#     rating = columns.Integer()
#     created_at = columns.DateTime(default=datetime.utcnow)
#
#
#     class Meta:
#         db_table = "feedbacks"
#         get_pk_field = 'feedback_id'
#         app_label = "cassandra_app"
#



# new test==================

from django.db import models
from mongoengine import Document, StringField, FloatField, DateTimeField
from datetime import datetime

# -------------------------
# PostgreSQL -> User
# -------------------------
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'


# -------------------------
# MongoDB -> Product
# -------------------------
class Product(Document):
    name = StringField(max_length=200, required=True)
    description = StringField()
    price = FloatField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {'collection': 'products'}


# -------------------------
# MySQL -> Payment
# -------------------------
class Payment(models.Model):
    user_id = models.IntegerField()
    product_id = models.CharField(max_length=100)
    amount = models.FloatField()
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payments'




