from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView


def list_books(request):
      all_the_books = Book.objects.all()
      context = {'books': all_the_books}
      return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
