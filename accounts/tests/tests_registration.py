from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import RegisterationSerializer

User = get_user_model()


class RegistrationAPITest(APITestCase):
    def test_normal_registration(self):
        url = "/accounts/register/"

        # Create a valid registration payload
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.data["status"], "success")
        self.assertIn("data", response.data)
        data = response.data["data"]
        self.assertIn("tokens", data)
        tokens = data["tokens"]
        self.assertIn("refresh", tokens)
        self.assertIn("access", tokens)
        self.assertEqual(User.objects.count(), 1)  # Ensure a user is created

    def test_google_registration(self):
        url = "/accounts/register/"

        # Create a valid Google registration payload
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "google_id": "google123",
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "success")
        self.assertIn("data", response.data)
        data = response.data["data"]
        self.assertIn("tokens", data)
        tokens = data["tokens"]
        self.assertIn("refresh", tokens)
        self.assertIn("access", tokens)
        self.assertEqual(User.objects.count(), 1)  # Ensure a user is created

    def test_invalid_registration(self):
        url = "/accounts/register/"

        # Create an invalid registration payload
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            # Missing the 'password' field
        }

        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("tokens", response.data)
        self.assertEqual(User.objects.count(), 0)  # Ensure no user is created
