from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Wishlist, Quote, Bookshelf
from .serializers import WishlistSerializer, QuoteSerializer, BookshelfSerializer


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getWishlist(request):
    if (request.method == 'GET'):
        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getQuotes(request):
    if (request.method == 'GET'):
        quotes = Quote.objects.filter(user=request.user)
        serializer = QuoteSerializer(quotes, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getBookshelf(request):
    if (request.method == 'GET'):
        bookshelf = Bookshelf.objects.filter(user=request.user)
        serializer = BookshelfSerializer(bookshelf, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)