from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListCreateAPIView,
    BookDetailAPIView,
    CategoryViewSet,
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView
)

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view()),
    path("books/<int:id>/", BookDetailAPIView.as_view()),

    path("auth/register/", RegisterAPIView.as_view()),
    path("auth/login/", LoginAPIView.as_view()),
    path("auth/logout/", LogoutAPIView.as_view()),

    path("", include(router.urls)),
]
