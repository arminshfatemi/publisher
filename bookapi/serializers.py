from rest_framework import serializers
from products.models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'is_enable')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('name', 'description', 'author', 'category', 'is_enable', 'file', 'created_time')

        # 'author', 'category', 'is_enable', 'file', 'created_time')

class BookDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('name', 'description', 'author', 'category', 'is_enable', 'file', 'created_time')