from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Author, Book, Rate, Review
from .serializers import AuthorSerializer, AuthorInfoSerializer, BookSerializer, RateSerializer, \
    ReviewSerializer, ReviewShortSerializer

def get_books(request):
    if(request.method == 'GET'):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

def get_authors(request):
    if(request.method == 'GET'):
        authors = Author.objects.all()
        serialized = AuthorSerializer(authors, many=True)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)
    return HttpResponse(status=404)

def get_author_info(request, pk):
    if(request.method == 'GET'):
        try:
            author = Author.objects.get(id=pk)
        except Author.DoesNotExist:
            return HttpResponse(status=404)

        serialized = AuthorInfoSerializer(author)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)
    return HttpResponse(status=404)

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if(request.method == 'GET'):
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

def getBookReviews(request, pk):
    if(request.method == 'GET'):
        try:
            reviews = Review.objects.filter(book=pk)
        except Book.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    return HttpResponse(status=404)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def rate_book(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = RateSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def review_book(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = ReviewShortSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def iswrote_review(request, pk):
    if(request.method == 'GET'):
        try:
            review = Review.objects.get(user=request.user, book=pk)
        except Review.DoesNotExist:
            return HttpResponse(status=404)

        return HttpResponse(status=200)
    return HttpResponse(status=404)
