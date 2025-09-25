# cassandra_app/apps.py
from django.apps import AppConfig
from django.conf import settings
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

class CassandraAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cassandra_app'

    def ready(self):
        # import Feedback here, inside ready(), not at top-level
        from .models import Feedback

        connection.setup(
            hosts=settings.CASSANDRA_NODES,
            default_keyspace=settings.CASSANDRA_KEYSPACE,
            protocol_version=5
        )
        sync_table(Feedback)
