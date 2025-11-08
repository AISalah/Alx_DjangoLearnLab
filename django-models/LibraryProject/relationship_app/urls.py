from django.urls import path
# Use one clean import line for the specific views you need
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='books-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]