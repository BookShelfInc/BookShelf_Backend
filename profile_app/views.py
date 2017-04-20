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
def get_wishlist(request):
    if (request.method == 'GET'):
        wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(wishlist, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def addbookto_wishlist(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = WishlistSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_wishlist(request, pk):
    try:
        wishlist = Wishlist.objects.get(pk=pk)
    except Wishlist.DoesNotExist:
        return HttpResponse(status=404)
    if(request.method == 'POST'):
        wishlist.delete()
        return HttpResponse(status=200)

##################
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def get_quotes(request):
    if (request.method == 'GET'):
        quotes = Quote.objects.filter(user=request.user)
        serializer = QuoteSerializer(quotes, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def add_quote(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = QuoteSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_quote(request, pk):
    try:
        quote = Quote.objects.get(pk=pk)
    except Quote.DoesNotExist:
        return HttpResponse(status=404)
    if(request.method == 'POST'):
        quote.delete()
        return HttpResponse(status=200)

##################
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def get_bookshelf(request):
    if (request.method == 'GET'):
        bookshelf = Bookshelf.objects.filter(user=request.user)
        serializer = BookshelfSerializer(bookshelf, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def manage_bookshelf(request, pk):
    try:
        bookshelf = Bookshelf.objects.get(pk=pk)
    except Bookshelf.DoesNotExist:
        return HttpResponse(status=404)

    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = BookshelfAddSerializer(data=data)
        if (serialized.is_valid()):

            for bookId in serialized.data['books']:
                bookshelf.books.add(Book.objects.get(id=bookId))
            bookshelf.save()

            return JsonResponse(serialized.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method == 'DELETE'):
        data = JSONParser().parse(request)
        serialized = BookshelfAddSerializer(data=data)
        if (serialized.is_valid()):
            for bookId in serialized.data['books']:
                bookshelf.books.remove(Book.objects.get(id=bookId))
            bookshelf.save()

            return JsonResponse(serialized.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_bookshelf(request, pk):
    try:
        bookshelf = Bookshelf.objects.get(pk=pk)
    except Bookshelf.DoesNotExist:
        return HttpResponse(status=404)

    if(request.method == 'POST'):
        bookshelf.delete()
        return HttpResponse(status=200)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def create_bookshelf(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = BookshelfSerializer(data=data)
        if(serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
