from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, AuthorViewSet, BookViewSet, FavoriteViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'favorites', FavoriteViewSet, basename='favorite')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]