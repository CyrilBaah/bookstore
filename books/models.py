from django.db import models
from isbn_field import ISBNField


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isbn = ISBNField()
    cover_image = models.ImageField(upload_to="book_covers/", null=True, blank=True)
