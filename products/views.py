from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import BookForm
from .models import Category, Author, Book


class BookListView(ListView):
    model = Book
    template_name = 'products/allposts.html'
    context_object_name = 'books'

    def get_queryset(self, *args, **kwargs):
        qs = super(BookListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


#    paginate_by = 1
#    print(Book.objects.all())


class BookDetailView(DetailView):
    model = Book
    template_name = 'products/detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = "products/bookcreate.html"
    #form_class = BookForm
    fields = ["name", "description", "author", "category", "is_enable", "file"]
