from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Implementing User Authentication in Django
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# For the checker
# At the top of relationship_app/views.py

# ... other imports ...
from django.contrib.auth import login



def list_books(request):
      all_the_books = Book.objects.all()
      context = {'books': all_the_books}
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

# Implementing User Authentication in Django
# Registration
# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # You might need to change this redirect later
            return redirect('books-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

