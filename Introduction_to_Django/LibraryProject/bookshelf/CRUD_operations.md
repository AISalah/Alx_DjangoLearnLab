##Create

#Python command
from bookshelf.models import Boo
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#comment with output
<Book: Book object (1)>

##Retrieve

#Python command
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

#comment with output
Title: 1984, Author: George Orwell, Year: 1949

##Update

#Python command
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = 'Nineteen Eighty-Four'
book.save()
book = Book.objects.get(publication_year=1949)
print(book.title)

#comment with output
Nineteen Eighty-Four



##Delete

#Python command
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
book.save()
Book.objects.all()

#comment with output
(1, {'bookshelf.Book': 1})
<QuerySet []>