#Python command
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = 'Nineteen Eighty-Four'
book.save()
book = Book.objects.get(publication_year=1949)
print(book.title)

#comment with output
Nineteen Eighty-Four
