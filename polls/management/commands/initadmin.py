from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_user(username= 'admin',
                                email='admin@example.com',
                                password='password',
                                is_staff=True,
                                is_active=True,
                                is_superuser=True
        )
        else:
            print('Admin accounts can only be initialized if no Accounts exist')