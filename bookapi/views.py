from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from products.models import Book
from .serializers import BookSerializer


class BookListView(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True, context={'request': request})
        return Response(serializer.data)
