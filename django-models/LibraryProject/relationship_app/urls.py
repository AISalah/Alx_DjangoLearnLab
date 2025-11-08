from django.urls import path
from . import  views
from .views import list_all_books, LibraryDetailView


urlpatterns = [
    path('books/', views.list_all_books, name='books-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]