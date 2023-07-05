from django.urls import path
from .views import BookListView, BookDetailView,BookCreateView, AboutView

urlpatterns = [
    path('allbooks/', BookListView.as_view(), name='allbooks'),
    path('allbooks/<int:pk>/', BookDetailView.as_view(),),
    path('allbooks/createbook/', BookCreateView.as_view(), name="createbook"),
    path('about/', AboutView, name="about"),


]
