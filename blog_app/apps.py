from django.apps import AppConfig
from django.db.utils import OperationalError


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'

    def ready(self):
        try:
            from .models import Genre
            genres = ["Technology", "Adventure", "Food", "Lifestyle", "Education"]

            for g in genres:
                Genre.objects.get_or_create(name=g)

        except OperationalError:
            pass