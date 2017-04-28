from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import BazaarBook
from .serializers import BazaarBookSerializer

def get_all_ads(request):
    if(request.method == 'GET'):
        book_ads = BazaarBook.objects.all()
        serialized = BazaarBookSerializer(book_ads, many=True)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)

def get_ad(request, pk):
    if(request.method == 'GET'):
        try:
            ad = BazaarBook(pk=pk)
        except BazaarBook.DoesNotExist:
            return HttpResponse(status=404)
        serialized = BazaarBookSerializer(ad)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)
    return HttpResponse(status=404)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def create_bazaar_ad(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = BazaarBookSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_bazaar_ad(request, pk):
    if(request.method == 'POST'):
        try:
            bazaar_ad = BazaarBook(pk=pk)
        except BazaarBook.DoesNotExist:
            return HttpResponse(status=404)

        bazaar_ad.delete()
        return HttpResponse(status=200)
