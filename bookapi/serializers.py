from rest_framework import serializers
from products.models import Book


class BookSerializer(serializers.ModelSerializer):
    category = serializers.ModelSerializer(many=True)
    author = serializers.ModelSerializer(many=True)

    class Meta:
        model = Book
        fields = ['name', 'description', 'author', 'category', 'is_enable', 'file' , 'created_time']