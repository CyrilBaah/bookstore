from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class LoginAPITest(APITestCase):
    def test_login_with_credentials(self):
        url = "/accounts/login/"

        # Create a user to use for login
        User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )

        # Prepare the login payload
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertIn("data", response.data)
        data = response.data["data"]
        self.assertIn("tokens", data)
        tokens = data["tokens"]
        self.assertIn("refresh", tokens)
        self.assertIn("access", tokens)

    def test_login_with_google_id_and_email(self):
        url = "/accounts/login/"

        # Create a user to use for login with Google ID and email
        User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            google_id="google123",
        )

        # Prepare the Google login payload
        payload = {
            "google_id": "google123",
            "email": "testuser@example.com",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertIn("data", response.data)
        data = response.data["data"]
        self.assertIn("tokens", data)
        tokens = data["tokens"]
        self.assertIn("refresh", tokens)
        self.assertIn("access", tokens)

    def test_login_with_invalid_credentials(self):
        url = "/accounts/login/"

        # Prepare an invalid login payload
        payload = {
            "username": "testuser",
            "password": "wrongpassword",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("tokens", response.data)

    def test_login_with_invalid_google_credentials(self):
        url = "/accounts/login/"

        # Prepare an invalid Google login payload
        payload = {
            "google_id": "invalid_google_id",
            "email": "testuser@example.com",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotIn("tokens", response.data)
