from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Author, Book, Rate, Review
from .serializers import AuthorSerializer, BookSerializer, RateSerializer, ReviewSerializer

def get_books(request):
    if(request.method == 'GET'):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

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
        serialized = ReviewSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def iswrote_review(request):
    if(request.method == 'POST'):
        try:
            review = Review.objects.filter(user=request.user)
        except Review.DoesNotExist:
            return HttpResponse(status=404)

        if(review.count() > 0):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    return HttpResponse(status=404)
