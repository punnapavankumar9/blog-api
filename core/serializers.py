from rest_framework import serializers
from core.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'blog_pic']
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)