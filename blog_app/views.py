from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post, Comment, Upvote
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer, CommentCreateSerializer, UpvoteSerializer

def get_all_posts(request):
    if(request.method == 'GET'):
        posts = Post.objects.all()
        serialized = PostSerializer(posts, many=True)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def get_user_posts(request):
    if (request.method == 'POST'):
        bookshelf = Post.objects.filter(author=request.user)
        serializer = PostSerializer(bookshelf, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def create_post(request):
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = PostCreateSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_post(request, pk):
    if(request.method == 'POST'):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return HttpResponse(status=404)

        post.delete();
        return HttpResponse(status=200)


def get_post_info(request, pk):
    if(request.method == 'GET'):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return HttpResponse(status=404)

        serialized = PostSerializer(post)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def create_comment(request):
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = CommentCreateSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def delete_comment(request, pk):
    if(request.method == 'POST'):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return HttpResponse(status=404)

        comment.delete();
        return HttpResponse(status=200)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def create_upvote(request):
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serialized = UpvoteSerializer(data=data)
        if (serialized.is_valid()):
            serialized.save()
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def is_liked(request, pk):
    if (request.method == 'GET'):
        try:
            upvote = Upvote.objects.filter(author=request.user, post=pk)
        except Upvote.DoesNotExist:
            return HttpResponse(status=404)

        if(upvote.count() > 0):
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
