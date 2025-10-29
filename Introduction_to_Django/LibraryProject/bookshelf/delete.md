#Python command
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
book.save()
Book.objects.all()

#comment with output
(1, {'bookshelf.Book': 1})
<QuerySet []>