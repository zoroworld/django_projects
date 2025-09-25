from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback
import uuid
from datetime import datetime

# Create your views here.

# ----------------- Cassandra -----------------

def create_feedback(request):
    user_id = int(request.GET.get('user_id', 1))
    product_id = request.GET.get('product_id', 'prod-1')
    comment = request.GET.get('comment', 'Good product!')
    rating = int(request.GET.get('rating', 5))

    feedback = Feedback.create(
        feedback_id=uuid.uuid4(),
        user_id=user_id,
        product_id=product_id,
        comment=comment,
        rating=rating,
        created_at=datetime.utcnow()
    )
    return JsonResponse({
        'feedback_id': str(feedback.feedback_id),
        'comment': feedback.comment
    })
