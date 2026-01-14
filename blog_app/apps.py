from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'

    def ready(self):
        from .create_superuser import create_superuser
        create_superuser()