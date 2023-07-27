from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class ChangePasswordViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.url = "/accounts/change_password/"

        # Authenticate the user
        self.client.force_authenticate(user=self.user)

    def test_change_password(self):
        # Prepare the change password payload
        payload = {
            "old_password": "testpassword",
            "new_password": "newtestpassword",
        }

        response = self.client.put(self.url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertEqual(response.data["message"], "Password updated successfully")

        # Verify that the user's password has been updated
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newtestpassword"))

    def test_change_password_with_invalid_old_password(self):
        # Prepare an invalid change password payload with wrong old password
        payload = {
            "old_password": "wrongpassword",
            "new_password": "newtestpassword",
        }

        response = self.client.put(self.url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["old_password"][0], "Wrong password.")

        # Verify that the user's password remains unchanged
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("testpassword"))

    def test_change_password_with_missing_fields(self):
        # Prepare a change password payload with missing fields
        payload = {
            "old_password": "testpassword",
        }

        response = self.client.put(self.url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("new_password", response.data)

        # Verify that the user's password remains unchanged
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("testpassword"))
