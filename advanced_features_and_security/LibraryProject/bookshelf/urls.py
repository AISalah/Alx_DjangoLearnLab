from django.urls import path
from .views import books, create_book_view, edit_book_view, delete_book_view, view_book_view

urlpatterns = [
    path('', books, name='books'),
    path('create/', create_book_view, name='create'),
    path('delete/', delete_book_view, name='delete'),
    path('edit/', edit_book_view, name='edit'),
    path('view/', view_book_view, name='view'),

]