from rest_framework import serializers

from auth_app.serializers import UserSerializer
from book_app.serializers import BookSerializer
from .models import Wishlist, Quote, Bookshelf

class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'user',
            'book',
            'has_read'
        )

class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'user',
            'book',
            'has_read'
        )

class QuoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = Quote
        fields = (
            'id',
            'quote',
            'user',
            'book'
        )

class QuoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'id',
            'quote',
            'user',
            'book'
        )

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = (
            'id',
            'user',
            'name',
            'books',
        )

class BookshelfAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = (
            'books',
        )