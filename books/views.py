from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer


class BookCreateAPIView(APIView):
    """Create a new Book | Administrator"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookListAPIView(APIView):
    """List all Book"""
    
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication,)
    
    def get(self, request):
        serializer = BookSerializer()
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
