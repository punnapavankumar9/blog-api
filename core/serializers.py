from rest_framework import serializers
from core.models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    date_created = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'blog_pic', 'date_created']
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

class CommentSerailizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    blog = serializers.PrimaryKeyRelatedField(read_only=True)
    date_commented = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['content', 'user', 'blog', 'date_commented']
        