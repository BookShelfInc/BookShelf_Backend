from rest_framework import serializers

from .models import BazaarBook

class BazaarBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BazaarBook
        fields = (
            'id',
            'book',
            'user',
            'price',
            'publish_date',
        )