from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('allbooks/', BookListView.as_view(), name='allbooks'),
    path('allbooks/<int:pk>/', BookDetailView.as_view(), name='book_detail'),


]
