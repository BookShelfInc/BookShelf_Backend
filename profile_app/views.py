from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from book_app.models import Book

from .models import Wishlist, Quote, Bookshelf
from .serializers import WishlistSerializer, QuoteSerializer, BookshelfSerializer, BookshelfAddSerializer


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getWishlist(request):
    if (request.method == 'GET'):
        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def addBookToWishlist(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = WishlistSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

##################
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getQuotes(request):
    if (request.method == 'GET'):
        quotes = Quote.objects.filter(user=request.user)
        serializer = QuoteSerializer(quotes, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def addQuote(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = QuoteSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

##################
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getBookshelf(request):
    if (request.method == 'GET'):
        bookshelf = Bookshelf.objects.filter(user=request.user)
        serializer = BookshelfSerializer(bookshelf, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST', ])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def addBookToBookshelf(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = BookshelfAddSerializer(data=data)
        if (serialized.is_valid()):
            try:
                bookshelf = Bookshelf.objects.get(id=data['id'])
            except Bookshelf.DoesNotExist:
                return JsonResponse(status=status.HTTP_404_NOT_FOUND)

            for i in bookshelf.books.all():
                print(i.title)

            for bookId in serialized.data['books']:
                bookshelf.books.add(Book.objects.get(id=bookId))
            bookshelf.save()

            return JsonResponse(serialized.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def createBookshelf(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = BookshelfSerializer(data=data)
        if(serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
