from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

class BookListCreateAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailAPIView(GenericAPIView):
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self, id):
        return get_object_or_404(Book, id=id)

    def get(self, request, id):
        book = self.get_object(id)
        serializer = self.get_serializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        book = self.get_object(id)
        serializer = self.get_serializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, id):
        book = self.get_object(id)
        serializer = self.get_serializer(
            book, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        book = self.get_object(id)
        book.delete()
        return Response(
            {"detail": "Book deleted"},
            status=status.HTTP_200_OK
        )


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]




class LoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error": "Login yoki parol xato"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)
        return Response(
            {"message": "Logged in successfully"},
            status=status.HTTP_200_OK
        )


class RegisterAPIView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username va password majburiy"},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(
            username=username,
            password=password
        )
        return Response(
            {"message": "User created"},
            status=status.HTTP_201_CREATED
        )





class LogoutAPIView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"})
