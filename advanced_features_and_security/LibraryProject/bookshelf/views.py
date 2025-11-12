from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library Project homepage!")

def books(request):
    return HttpResponse("Welcome to the bookshelf!")
