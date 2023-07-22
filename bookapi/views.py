from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from products.models import Book
from .serializers import BookSerializer, BookDetailSerializer


class BookListView(APIView):

    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True, context={'request': request})
        return Response(serializer.data)


class BookDetailView(APIView):

    def get(self,request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)