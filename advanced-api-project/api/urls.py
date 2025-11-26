from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # 1. List all books (GET)
    path('books/', ListView.as_view(), name='book-list'),

    # 2. View details of one book (GET)
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),

    # 3. Create a new book (POST)
    path('books/create/', CreateView.as_view(), name='book-create'),

    # 4. Update a book (PUT/PATCH)
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),

    # 5. Delete a book (DELETE)
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]