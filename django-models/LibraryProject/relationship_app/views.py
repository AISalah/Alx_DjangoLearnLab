from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView


def list_all_books(request):
      all_the_books = Book.objects.all()
      context = {'books': all_the_books}
      return render(request, 'books/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'