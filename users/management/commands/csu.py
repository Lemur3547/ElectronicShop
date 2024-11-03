import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from config.settings import BASE_DIR
from users.models import User


class Command(BaseCommand):
    """Команда для создания суперюзера"""
    def handle(self, *args, **options):
        load_dotenv(BASE_DIR / '.env', override=True)
        user = User.objects.create(
            email=os.getenv('email'),
            first_name=os.getenv('first_name'),
            last_name=os.getenv('last_name'),
            phone=os.getenv('phone'),
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(os.getenv('password'))
        user.save()
