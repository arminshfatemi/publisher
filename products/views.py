from django.shortcuts import render
from .models import Category, Author, Book
from django.views.generic import ListView,DetailView


class BookListView(ListView):
    model = Book
    template_name = 'products/allposts.html'
    context_object_name = 'books'

#    paginate_by = 1
#    print(Book.objects.all())


class BookDetailView(DetailView):
    model = Book
    template_name = 'products/detail.html'
    context_object_name = 'book'
