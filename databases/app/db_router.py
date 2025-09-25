# class MultiDBRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == "postgres_app":
#             return "postgres_db"
#         elif model._meta.app_label == "mysql_app":
#             return "mysql_db"
#         elif model._meta.app_label == "cassandra_app":
#             return "cassandra_db"
#         # Default apps go to default
#         return "default"
#
#     def db_for_write(self, model, **hints):
#         return self.db_for_read(model, **hints)
#
#     def allow_relation(self, obj1, obj2, **hints):
#         # Allow if both objects are on the same DB
#         db_obj1 = self.db_for_read(obj1.__class__)
#         db_obj2 = self.db_for_read(obj2.__class__)
#         if db_obj1 and db_obj1 == db_obj2:
#             return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == "postgres_app":
#             return db == "postgres_db"
#         elif app_label == "mysql_app":
#             return db == "mysql_db"
#         elif app_label == "cassandra_app":
#             return db == "cassandra_db"
#         # Allow Django default apps on default DB
#         elif db == "default":
#             return True
#         return None


# diffrent
class DatabaseRouter:
    """
    Routes models to their appropriate databases
    """
    route_app_labels = {
        'User': 'default',        # PostgreSQL
        'Payment': 'mysql_db',    # MySQL
        # Product uses MongoEngine (not ORM) → no routing
        # Feedback uses Cassandra → handled by django_cassandra_engine
    }

    def db_for_read(self, model, **hints):
        if model.__name__ in self.route_app_labels:
            return self.route_app_labels[model.__name__]
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ in self.route_app_labels:
            return self.route_app_labels[model.__name__]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_list = set(self.route_app_labels.values())
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in self.route_app_labels:
            return db == self.route_app_labels[model_name]
        return None
