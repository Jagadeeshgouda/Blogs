from rest_framework import serializers
from .models import BlogPost, BlogContent

class BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = ('id','content_type', 'media_file')

class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    contents = BlogContentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id','user', 'title', 'description', 'created_at', 'contents')
