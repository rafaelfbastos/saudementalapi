from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username=os.getenv('SUPER_USER', 'change-me'),
                password=os.getenv('SUPER_USER_PASSWORD', 'change-me')
            )
        print('Superuser has been created.')