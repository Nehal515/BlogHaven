import os
from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    if User.objects.filter(is_superuser=True).exists():
        return

    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

    if not username or not password:
        return

    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
