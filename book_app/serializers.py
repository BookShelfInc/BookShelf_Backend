from rest_framework import serializers

from .models import Author, Book, Rate, Review

from auth_app.serializers import UserSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'biography',
            'avatar',
        )

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'author',
            'genre',
            'cover',
        )

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'user',
            'book',
            'rating',
        )

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = (
            'user',
            'book',
            'review',
        )

class AuthorInfoSerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'biography',
            'avatar',
            'book_set',
        )
