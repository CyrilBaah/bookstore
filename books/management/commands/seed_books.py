from django.core.management.base import BaseCommand
from faker import Faker

from books.models import Book


class Command(BaseCommand):
    help = "Seeds the Book table with fake data"

    def handle(self, *args, **options):
        fake = Faker()
        genres = [
            "Fiction",
            "Romance",
            "Mystery",
            "Science Fiction",
            "Thriller",
            "Historical Fiction",
            "Literature",
        ]
        # Create 100 books with fake data
        for _ in range(100):
            book = Book()
            book.title = fake.text(max_nb_chars=50)
            book.author = fake.name()
            book.price = fake.pydecimal(left_digits=2, right_digits=1, positive=True)
            book.isbn = fake.isbn13()
            book.genre = fake.random_element(elements=genres)
            book.cover_image = "https://unsplash.com/photos/RrhhzitYizg"

            book.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Book table"))
