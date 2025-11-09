from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# Use one clean import line for the specific views you need
from .views import list_books, LibraryDetailView, register, admin_view, librarian_view, member_view
from . import views


urlpatterns = [
    path('books/', list_books, name='books-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/login.html'), name='logout'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]

