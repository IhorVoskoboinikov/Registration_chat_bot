import os
from asgiref.sync import sync_to_async

from django.core.wsgi import get_wsgi_application
from django.db import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_bot_registration.settings')

application = get_wsgi_application()

from django.contrib.auth.models import User
from .models import ClientProfile


@sync_to_async
def save_user_data(user_dict: dict) -> bool:
    try:
        user = User.objects.create_user(
            username=user_dict['login'],
            password=user_dict['password']
        )
        client_data = ClientProfile(
            user=user,
            user_name=user_dict['user_name'],
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            phone=user_dict['phone'],
            photo=user_dict['photo'],
        )
        client_data.save()
        return True
    except IntegrityError:
        return False
