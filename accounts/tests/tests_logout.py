from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


# class UserLogoutAPIViewTestCase(APITestCase):
#     def setUp(self):
#         # Create a user and obtain a valid refresh token
#         self.user = User.objects.create_user(
#             username="testuser", email="testuser@example.com", password="testpassword"
#         )
#         self.token = RefreshToken.for_user(self.user)
#         self.access_token = str(self.token.access_token)

#     def perform_logout_request(self, refresh_token=None):
#         url = reverse("logout_user")

#         # Set an invalid access token in the Authorization header
#         headers = {
#             "Authorization": f"Bearer {self.access_token}",
#         }

#         # Set the refresh token in the request body
#         data = {"refresh": str(refresh_token)} if refresh_token else {}

#         return self.client.post(url, headers=headers, data=data)

#     def test_user_logout_with_valid_refresh_token(self):
#         response = self.perform_logout_request(refresh_token=self.token)
#         expected_status = status.HTTP_205_RESET_CONTENT

#         self.assertEqual(response.status_code, expected_status)
#         self.assertEqual(response.json()["status"], "success")
#         self.assertEqual(response.json()["message"], "Logout successfully")

#     def test_user_logout_without_refresh_token(self):
#         response = self.perform_logout_request()
#         expected_status = status.HTTP_400_BAD_REQUEST

#         self.assertEqual(response.status_code, expected_status)

#     def test_user_logout_with_invalid_refresh_token(self):
#         bad_token = "invalidtoken"
#         response = self.perform_logout_request(refresh_token=bad_token)
#         expected_status = status.HTTP_400_BAD_REQUEST

#         self.assertEqual(response.status_code, expected_status)
