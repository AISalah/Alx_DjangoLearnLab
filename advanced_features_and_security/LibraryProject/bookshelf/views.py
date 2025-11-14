from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ExampleForm


def home(request):
    return HttpResponse("Welcome to the Library Project homepage!")

def books(request):
    return HttpResponse("Welcome to the bookshelf!")


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    all_the_books = Book.objects.all()
    context = {'books': all_the_books}
    return render(request, 'bookshelf/book_list.html', context)


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book_view(request):
    return HttpResponse("you can CREATE books")
    # return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book_view(request):
    return HttpResponse("You can EDIT books!")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book_view(request):
    return HttpResponse("You can DELETE books!")

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book_view(request):
    return HttpResponse("You only can VIEW books!")


def form_example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})