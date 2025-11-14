from django.urls import path
from .views import create_book_view, edit_book_view, delete_book_view, view_book_view, book_list

urlpatterns = [
    path('', book_list, name='books-list'),
    path('create/', create_book_view, name='create'),
    path('delete/', delete_book_view, name='delete'),
    path('edit/', edit_book_view, name='edit'),
    path('view/', view_book_view, name='view'),
    # path('<int:pk>/delete/', delete_book_view, name='delete'),
    # path('<int:pk>/edit/', edit_book_view, name='edit'),
    # path('<int:pk>/view/', view_book_view, name='view'),
]