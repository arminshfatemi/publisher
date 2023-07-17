from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .forms import BookForm
from .models import Category, Author, Book


class BookListView(ListView):
    model = Book
    template_name = 'products/allposts.html'
    context_object_name = 'books'
    paginate_by = 1

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
    # form_class = BookForm
    fields = ["name", "description", "author", "category", "is_enable", "file"]


def AboutView(request):
    return render(request, 'products/about.html')


def SearchView(request):
    posts = Book.objects.order_by('-created_time').filter(is_enable=True)

    if 'search_text' in request.GET:
        search_text = request.GET['search_text']

        if search_text:
            posts = posts.filter(Q(name__contains=search_text)
                                 | Q(description__contains=search_text)
                                 | Q(author__name__contains=search_text))
    context = {
        'posts': posts
    }

    return render(request, 'products/search.html', context)
