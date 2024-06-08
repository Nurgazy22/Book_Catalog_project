from rest_framework import serializers
from .models import Genre, Author, Book, Favorite, Review
from django.db.models import Avg


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'text', 'created_at']


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    genre = GenreSerializer()
    author = AuthorSerializer()
    average_rating = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'author', 'publication_date', 'description', 'reviews', 'average_rating', 'is_favorite']

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(book=obj)
        if reviews.exists():
            return reviews.aggregate(average=Avg('rating'))['average']
        return None

    def get_is_favorite(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return Favorite.objects.filter(book=obj, user=user).exists()
        return False


class FavoriteSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_detail = BookSerializer(source='book', read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'book_detail', 'user']
        read_only_fields = ['user']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['book'] = BookSerializer(instance.book, context=self.context).data
        return response



