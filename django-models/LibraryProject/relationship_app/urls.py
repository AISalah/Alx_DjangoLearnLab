from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# Use one clean import line for the specific views you need
from .views import list_books, LibraryDetailView, register
from . import views


urlpatterns = [
    path('books/', list_books, name='books-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
]