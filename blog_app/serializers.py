from rest_framework import serializers

from .models import Post, Comment, Upvote
from auth_app.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'publish_date',
            'author',
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'publish_date',
            'author',
            'post',
        )

class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = (
            'id',
            'author',
            'post',
            'like'
        )