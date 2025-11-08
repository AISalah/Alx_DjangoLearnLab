from django.contrib import admin
# Import all the models from your app's models.py
from .models import Author, Book, Library, Librarian

# Register each model with the admin site
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)