from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin user if it does not exist"

    def handle(self, *args, **options):
        if (
            User.objects.filter(is_staff=True, username=settings.ADMIN_USERNAME).count()
            > 0
        ):
            self.stdout.write(
                f"Admin user {settings.ADMIN_USERNAME} " f"Already exists "
            )
            return

        User.objects.create_superuser(
            username=settings.ADMIN_USERNAME,
            password=settings.ADMIN_PASSWORD,
            email="",
        )

        self.stdout.write(f"Admin user {settings.ADMIN_USERNAME} ")
