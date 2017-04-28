from rest_framework import serializers

from .models import BazaarBook

from auth_app.serializers import UserSerializer
from book_app.serializers import BookSerializer

class BazaarBookSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    class Meta:
        model = BazaarBook
        fields = (
            'id',
            'book',
            'user',
            'price',
            'publish_date',
        )