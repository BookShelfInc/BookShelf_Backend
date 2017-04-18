from rest_framework import serializers

from book_app.serializers import BookSerializer
from .models import Wishlist, Quote, Bookshelf

class WishlistSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Wishlist
        fields = (
            'user',
            'book',
            'has_read'
        )

class QuoteSerializer(serializers.ModelSerializer):
    book = BookSerializer()
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
            'books'
        )