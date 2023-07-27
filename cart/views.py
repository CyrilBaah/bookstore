from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Cart
from .serializers import CartSerializer


class CartCreateView(APIView):
    """Create a new Cart"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "code": status.HTTP_201_CREATED,
                "message": "Cart Created successfully",
                "data": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListView(APIView):
    """List all carts | Administrators"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        exercises = Cart.objects.all()
        total_carts = Cart.objects.count()
        serializer = CartSerializer(exercises, many=True)
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "All Cart Available",
            "total_cart": total_carts,
            "data": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


class CartDetailView(APIView):
    """List My Cart"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        carts = Cart.objects.filter(user=user_id)

        serializer = CartSerializer(carts, many=True)
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "My Carts",
            "data": serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)


class CartDeleteAPIView(APIView):
    """Delete a Cart"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def delete(self, request):
        user = request.user
        carts = Cart.objects.filter(user=user)
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
