from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Book
from ..serializers import BookSerializer

User = get_user_model()


class BookListAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
        )

    def test_list_books(self):
        url = "/books/"

        # Create some test books
        book1 = Book.objects.create(
            title="Book 1",
            author="Author 1",
            price="9.99",
            isbn="9783161484100",
            cover_image="https://example.com/book1.jpg",
        )
        book2 = Book.objects.create(
            title="Book 2",
            author="Author 2",
            price="19.99",
            isbn="9783161484101",
            cover_image="https://example.com/book2.jpg",
        )

        # Authenticate the user
        self.client.force_authenticate(user=self.user)

        # Send a GET request to retrieve the list of books
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the returned data matches the serialized data
        expected_data = BookSerializer([book1, book2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_list_books_unauthenticated(self):
        url = "/books/"

        # Send a GET request to retrieve the list of books without authentication
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
