# cassandra_app/models.py
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import uuid
from datetime import datetime

class Feedback(Model):
    __keyspace__ = "cassandra_keyspace"

    feedback_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    user_id = columns.Integer()
    product_id = columns.Text()
    comment = columns.Text()
    rating = columns.Integer()
    created_at = columns.DateTime(default=datetime.utcnow)

    class Meta:
        app_label = "cassandra_app"
        get_pk_field = 'feedback_id'
