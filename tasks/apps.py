from django.apps import AppConfig

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        pass  # Tạm thời bỏ import signals vì không cần thiết cho tasks app