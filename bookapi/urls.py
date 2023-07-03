from django.urls import path
from .views import BookListView

urlpatterns = [
    path('api/allbooks/', BookListView.as_view(), name='apiallbooks'),

]
