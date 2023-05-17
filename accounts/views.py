from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import(RegisterationSerializer)

User = get_user_model()

class RegistrationAPIView(GenericAPIView):
    """Registration API View."""
    permission_classes = (AllowAny,)
    serializer_class = RegisterationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid(): 
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