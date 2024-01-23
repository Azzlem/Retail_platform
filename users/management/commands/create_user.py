import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('USER_EMAIL'),
            is_staff=False,
            is_superuser=False,
            role='user',
            is_active=True,
        )

        user.set_password(os.getenv('USER_PASSWORD'))
        user.save()
