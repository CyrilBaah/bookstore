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

    def perform_refresh_token_request(self, refresh_token=None):
        url = "/accounts/token/refresh/"

        # Set the Authorization header with the access token
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }

        # Set the refresh token in the request body
        data = {"refresh": str(refresh_token)} if refresh_token else {}

        return self.client.post(url, headers=headers, data=data)

    def test_token_refresh(self):
        response = self.perform_refresh_token_request(refresh_token=self.token)
        expected_status = status.HTTP_200_OK

        self.assertEqual(response.status_code, expected_status)

    def test_token_refresh_with_invalid_token(self):
        bad_token = "invalid_token"
        response = self.perform_refresh_token_request(refresh_token=bad_token)
        expected_status = status.HTTP_401_UNAUTHORIZED

        self.assertEqual(response.status_code, expected_status)

    def test_token_refresh_without_token(self):
        response = self.perform_refresh_token_request()
        expected_status = status.HTTP_400_BAD_REQUEST

        self.assertEqual(response.status_code, expected_status)
