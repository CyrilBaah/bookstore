import os
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Book

User = get_user_model()


class BookDeleteAPITest(APITestCase):
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )
        # Create a normal user
        self.normal_user = User.objects.create_user(
            username="normal_user",
            email="normal_user@example.com",
            password="password123",
        )
        # Create a book for deletion
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            price='9.99',  
            isbn="9783161484100",
            cover_image="https://unsplash.com/photos/RrhhzitYizg",
        )

    def test_delete_book(self):
        self.client.force_authenticate(user=self.admin_user)
        url = f"/books/delete/{self.book.pk}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthorized(self):
        self.client.force_authenticate(user=self.normal_user)
        url = f"/books/delete/{self.book.pk}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)
