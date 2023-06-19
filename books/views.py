from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer


class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class BookCreateAPIView(APIView):
    """Create a new Book | Administrator"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "code": status.HTTP_201_CREATED,
                "message": "Book Created successfully",
                "data": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListAPIView(APIView):
    """List all Book"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    pagination_class = BookPagination

    def get(self, request):
        books = Book.objects.all()
        paginator = self.pagination_class()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "Books retrieved successfully",
            "data": serializer.data,
        }
        return paginator.get_paginated_response(response)


class BookUpdateAPIView(APIView):
    """Update a Book | Administrator"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    serializer_class = BookSerializer

    def put(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        if not book:
            return Response(
                {"detail": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Book Updated successfully",
                "data": data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    """Delete an book"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    serializer_class = BookSerializer

    def delete(self, request, pk, *args, **kwargs):
        book = Book.objects.filter(id=pk).first()
        if not book:
            return Response(
                {"detail": "book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        response = {
            "status": "success",
            "code": status.HTTP_204_NO_CONTENT,
            "message": "book deleted successfully",
        }
        return Response(response, status.HTTP_204_NO_CONTENT)
