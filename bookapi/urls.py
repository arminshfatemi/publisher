from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('api/allbooks/', BookListView.as_view(), name='apiallbooks'),
    path('api/book/<int:pk>/',BookDetailView.as_view(),)

]
