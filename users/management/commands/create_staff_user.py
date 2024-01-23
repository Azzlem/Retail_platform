import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('STAFF_USER_EMAIL'),
            is_staff=True,
            is_superuser=False,
            role='admin',
            is_active=True,
        )

        user.set_password(os.getenv('STAFF_USER_PASSWORD'))
        user.save()
