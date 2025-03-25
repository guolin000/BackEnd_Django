from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=False, write_only=False)  # 添加 content 字段

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'dynasty', 'cover', 'year', 'content_file', 'content_encoding', 'content']
