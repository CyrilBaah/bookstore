import secrets

from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """CustomUser Serializer"""

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class RegisterationSerializer(serializers.ModelSerializer):
    """Registration Serializer"""

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "google_id")
        extra_kwargs = {"password": {"write_only": True, "required": False}}


    def create(self, validated_data):
        # Check if google_id is present in the validated data
        if "google_id" in validated_data:
            # If so, create a Google user
            password = secrets.token_urlsafe(32)
            return CustomUser.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                google_id=validated_data["google_id"],
                password=password,
            )
        else:
            # Otherwise, create a normal user
            return CustomUser.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )