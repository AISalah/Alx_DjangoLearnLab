from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

def home(request):
    return HttpResponse("Welcome to the Library Project homepage!")

def books(request):
    return HttpResponse("Welcome to the bookshelf!")



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