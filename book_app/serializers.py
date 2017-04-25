from rest_framework import serializers

from .models import Author, Book, Rate, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            'biography',
        )

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
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
    class Meta:
        model = Review
        fields = (
            'user',
            'book',
            'review',
        )
