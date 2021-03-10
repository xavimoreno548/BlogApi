from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from apps.post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']