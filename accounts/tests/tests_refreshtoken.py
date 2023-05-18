from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class TokenRefreshTestCase(APITestCase):
    def setUp(self):
        # Create a user and obtain an access token
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.token = RefreshToken.for_user(self.user)
        self.access_token = str(self.token.access_token)

    def test_token_refresh(self):
        url = "/accounts/token/refresh/"

        # Set the Authorization header with the access token
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        # Set the refresh token in the request body
        data = {
            "refresh": str(self.token),
        }

        response = self.client.post(url, headers=headers, data=data)
        expected_status = status.HTTP_200_OK

        self.assertEqual(response.status_code, expected_status)

    def test_token_refresh_with_invalid_token(self):
        url = "/accounts/token/refresh/"

        # Set an invalid access token in the Authorization header
        headers = {
            "Authorization": "Bearer invalid_token",
        }

        bad_token = "invalidtoken"
        data = {
            "refresh": str(bad_token),
        }

        response = self.client.post(url, headers=headers, data=data)
        expected_status = status.HTTP_401_UNAUTHORIZED

        self.assertEqual(response.status_code, expected_status)

    def test_token_refresh_without_token(self):
        url = "/accounts/token/refresh/"

        response = self.client.post(url)
        expected_status = status.HTTP_400_BAD_REQUEST

        self.assertEqual(response.status_code, expected_status)
