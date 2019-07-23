from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'author_username',
            'content'
        ]

    def get_author_username(self, obj: Comment):
        return obj.author.username


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, source="comment_set", read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'text',
            'comments',
            'created_date',
            'published_date',
            'image_post'
        ]


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, source='post_set')
    custom_field = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "posts",
            "custom_field"
        ]

    def get_custom_field(self, obj: User):
        return obj.get_full_name()
