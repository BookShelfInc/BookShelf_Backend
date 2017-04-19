from rest_framework import serializers

from .models import Author, Book, Rate

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
            'title',
            'description',
            'author',
            'genre',
        )

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'user',
            'book',
            'rating',
        )