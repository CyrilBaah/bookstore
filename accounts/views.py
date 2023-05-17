from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomUserSerializer, LoginSerializer, RegisterationSerializer

User = get_user_model()


class RegistrationAPIView(GenericAPIView):
    """Registration API View."""

    permission_classes = (AllowAny,)
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Normal Registration

            if (
                "username" in serializer.validated_data
                and "email" in serializer.validated_data
                and "password" in serializer.validated_data
            ):
                user = serializer.save()
                token = RefreshToken.for_user(user)
                data = serializer.data
                response = {
                    "status": "success",
                    "code": status.HTTP_201_CREATED,
                    "message": "Registration successful",
                    "data": data,
                }
                data["tokens"] = {
                    "refresh": str(token),
                    "access": str(token.access_token),
                }
                return Response(response, status=status.HTTP_201_CREATED)

            # Google Registration
            elif (
                "username" in serializer.validated_data
                and "email" in serializer.validated_data
                and "google_id" in serializer.validated_data
            ):
                user = serializer.save()
                token = RefreshToken.for_user(user)
                data = serializer.data
                response = {
                    "status": "success",
                    "code": status.HTTP_201_CREATED,
                    "message": "Registration successful",
                    "data": data,
                }
                data["tokens"] = {
                    "refresh": str(token),
                    "access": str(token.access_token),
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    """Login API view"""

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        if "google_id" in request.data:
            try:
                # Check if the google_id and email address exists
                google_id = request.data["google_id"]
                email = request.data["email"]

                user = User.objects.get(google_id=google_id, email=email)

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.validated_data
                serializer = CustomUserSerializer(user)
                token = RefreshToken.for_user(user)
                data = serializer.data
                response = {
                    "status": "success",
                    "code": status.HTTP_200_OK,
                    "message": "Login successful",
                    "data": data,
                }
                data["tokens"] = {
                    "refresh": str(token),
                    "access": str(token.access_token),
                }
                return Response(response, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response(
                    {"Error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )

        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            serializer = CustomUserSerializer(user)
            token = RefreshToken.for_user(user)
            data = serializer.data
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Login successful",
                "data": data,
            }
            data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
            return Response(response, status=status.HTTP_200_OK)
