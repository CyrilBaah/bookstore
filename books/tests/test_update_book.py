# import os

from django.contrib.auth import get_user_model

# from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Book

User = get_user_model()


class BookUpdateAPITest(APITestCase):
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpassword",
        )

        # Create a test book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            price="9.99",
            isbn="9783161484100",
            cover_image="https://example.com/book.jpg",
        )

    # def test_update_book(self):
    #     url = f"/books/update/{self.book.pk}/"

    #     # Authenticate the admin user
    #     self.client.force_authenticate(user=self.admin_user)

    # Prepare the updated book payload
    # updated_payload = {
    #     "title": "Book Updated successfully",
    #     "author": "Jane Smith",
    #     "price": "19.99",
    #     "isbn": "9783161484100",
    #     "cover_image": "https://example.com/updated-book.jpg",
    # }
    # # Add a cover image file to the payload
    # file_path = os.path.join(os.getcwd(), "book_covers/300.jpeg")
    # file_data = open(file_path, "rb").read()
    # file = SimpleUploadedFile("testimage.jpg", file_data, content_type="image/jpeg")
    # updated_payload["cover_image"] = file

    # response = self.client.post(url, payload=updated_payload, format="multipart")

    # # Send a PUT request to update the book
    # response = self.client.put(url, updated_payload)

    # self.assertEqual(response.status_code, status.HTTP_200_OK)

    # # Check if the book attributes have been updated correctly
    # self.assertEqual(response.data["data"]["title"], updated_payload["title"])
    # self.assertEqual(response.data["data"]["title"], updated_payload["title"])
    # self.assertEqual(response.data["data"]["author"], updated_payload["author"])
    # self.assertEqual(response.data["data"]["price"], updated_payload["price"])
    # self.assertEqual(response.data["data"]["isbn"], updated_payload["isbn"])
    # self.assertEqual(
    #     response.data["data"]["cover_image"], response.data["data"]["cover_image"]
    # )

    def test_update_book_not_found(self):
        url = "/books/update/999/"

        # Authenticate the admin user
        self.client.force_authenticate(user=self.admin_user)

        # Prepare the updated book payload
        updated_payload = {
            "title": "Updated Book",
            "author": "Jane Smith",
            "price": "19.99",
            "isbn": "9783161484101",
            "cover_image": "https://example.com/updated-book.jpg",
        }

        # Send a PUT request to update a non-existent book
        response = self.client.put(url, updated_payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_unauthorized(self):
        url = f"/books/update/{self.book.pk}/"

        # Prepare the updated book payload
        updated_payload = {
            "title": "Updated Book",
            "author": "Jane Smith",
            "price": "19.99",
            "isbn": "9783161484101",
            "cover_image": "https://example.com/updated-book.jpg",
        }

        # Send a PUT request to update the book without authentication
        response = self.client.put(url, updated_payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
