from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer

def register(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = UserSerializer(data=data)

        if(serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
