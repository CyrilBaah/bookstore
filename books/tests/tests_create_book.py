import os

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class BookCreateAPITest(APITestCase):
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )
        # Log in the admin user
        self.client.force_authenticate(user=self.admin_user)

    # def test_create_book(self):
    #     url = "/books/create/"

    #     # Prepare the book payload
    #     payload = {
    #         "title": "Test Book",
    #         "author": "John Doe",
    #         "price": "9.99",
    #         "isbn": "9783161484100",
    #         "cover_image": "https://unsplash.com/photos/RrhhzitYizg",
    #     }

    #     # Add a cover image file to the payload
    #     file_path = os.path.join(os.getcwd(), "book_covers/300.jpeg")
    #     file_data = open(file_path, "rb").read()
    #     file = SimpleUploadedFile("testimage.jpg", file_data, content_type="image/jpeg")
    #     payload["cover_image"] = file

    #     response = self.client.post(url, payload, format="multipart")

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data["data"]["title"], payload["title"])
    #     self.assertEqual(response.data["data"]["author"], payload["author"])
    #     self.assertEqual(response.data["data"]["price"], payload["price"])
    #     self.assertEqual(response.data["data"]["isbn"], payload["isbn"])
    #     self.assertIsNotNone(response.data["data"]["cover_image"])

    def test_create_book_invalid_data(self):
        url = "/books/create/"

        # Prepare an invalid book payload
        payload = {
            "title": "",
            "author": "John Doe",
            "price": "9.99",
            "isbn": "978-3-16-148410-0",
            "cover_image": "https://unsplash.com/photos/RrhhzitYizg",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("This field may not be blank.", response.data["title"])

    def test_create_book_unauthorized(self):
        url = "/books/create/"

        # Prepare the book payload
        payload = {
            "title": "Test Book",
            "author": "John Doe",
            "price": 9.99,
            "isbn": "978-3-16-148410-0",
            "cover_image": "https://unsplash.com/photos/RrhhzitYizg",
        }

        # Log out the admin user
        self.client.logout()

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_normal_user(self):
        url = "/books/create/"

        # Create a normal user
        normal_user = User.objects.create_user(
            username="normal_user",
            email="normal_user@example.com",
            password="password123",
        )
        # Log in the normal user
        self.client.force_authenticate(user=normal_user)

        # Prepare the book payload
        payload = {
            "title": "Test Book",
            "author": "John Doe",
            "price": "9.99",
            "isbn": "9783161484100",
            "cover_image": "https://unsplash.com/photos/RrhhzitYizg",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
