from django.core.management.base import BaseCommand
from faker import Faker

from books.models import Book


class Command(BaseCommand):
    help = "Seeds the Book table with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # Create 100 books with fake data
        for _ in range(100):
            book = Book()
            book.title = fake.text(max_nb_chars=50)
            book.author = fake.name()
            book.price = fake.pydecimal(left_digits=2, right_digits=1, positive=True)
            book.isbn = fake.isbn13()
            
            # You can modify the following lines based on your image handling logic
            # Generate or assign a fake cover image for the book
            cover_image = "https://unsplash.com/photos/RrhhzitYizg"

            # book.cover_image.save('book_covers/fake_cover.jpg', cover_image, save=True)
            
            book.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Book table"))
