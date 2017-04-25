from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
    return HttpResponse(status=400)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def getInfo(request):
    if(request.method == 'GET'):
        user = request.user
        serialized = UserSerializer(user)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK)
    return HttpResponse(status=400)
