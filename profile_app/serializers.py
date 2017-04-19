from rest_framework import serializers

from book_app.serializers import BookSerializer
from .models import Wishlist, Quote, Bookshelf

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'user',
            'book',
            'has_read'
        )

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'quote',
            'user',
            'book'
        )

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = (
            'user',
            'name',
            'books',
        )

class BookshelfAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = (
            'id',
            'books',
        )

    def create(self, validated_data):
        return Bookshelf.objects.create(**validated_data)