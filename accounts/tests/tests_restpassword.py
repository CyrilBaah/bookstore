from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class PasswordResetTestCase(APITestCase):
    # Create a user
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )

    def test_user_reset_password_request_with_valid_email(self):
        url = "/accounts/password_reset/"

        # Create a valid registration payload
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword",
        }

        response = self.client.post(url, payload)
        expected_status = status.HTTP_200_OK

        self.assertEqual(response.status_code, expected_status)

    def test_user_reset_password_request_with_invalid_email(self):
        url = "/accounts/password_reset/"

        # Create an invalid password reset payload with an unregistered email
        payload = {
            "email": "nonexistent@example.com",
        }

        response = self.client.post(url, payload)
        expected_status = status.HTTP_400_BAD_REQUEST

        self.assertEqual(response.status_code, expected_status)

    def test_user_reset_password_request_with_blank_email(self):
        url = "/accounts/password_reset/"

        # Create a password reset payload with a blank email
        payload = {
            "email": "",
        }

        response = self.client.post(url, payload)
        expected_status = status.HTTP_400_BAD_REQUEST

        self.assertEqual(response.status_code, expected_status)

    def test_user_reset_password_request_with_missing_email_field(self):
        url = "/accounts/password_reset/"

        # Create a password reset payload without the email field
        payload = {}

        response = self.client.post(url, payload)
        expected_status = status.HTTP_400_BAD_REQUEST

        self.assertEqual(response.status_code, expected_status)
