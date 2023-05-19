from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = "Seeds the User table with initial data"

    def handle(self, *args, **options):
        # Create the admin user
        admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@email.com",
            password="password123",
        )
        self.stdout.write(self.style.SUCCESS("Admin user created"))

        # Create the normal user
        normal_user = User.objects.create_user(
            username="usertest",
            email="usertest@gmail.com",
            password="password123",
        )
        self.stdout.write(self.style.SUCCESS("Normal user created"))

        # Create the Google user
        google_user = User.objects.create_user(
            username="google",
            email="google@gmail.com",
            password="password123",
            google_id="google123",
        )
        self.stdout.write(self.style.SUCCESS("Google user created"))
