# In relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian


def run_all_samples():
    print("--- Creating new sample data... ---")
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.R.R. Tolkien")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="The Hobbit", author=author2)

    library1 = Library.objects.create(name="City Central Library")
    library1.books.add(book1, book3)

    Librarian.objects.create(name="Alice Smith", library=library1)
    print("--- Sample data created successfully. ---\n")


    # Query 1: Query all books by a specific author.
    print("--- Query 1: Books by George Orwell ---")
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")

    # Query 2: List all books in a library.
    print("\n--- Query 2: Books in City Central Library ---")
    library_name = "City Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    for book in books_in_library:
        print(f"- {book.title}")

    # Query 3: Retrieve the librarian for a library.
    print("\n--- Query 3: Librarian for City Central Library ---")
    library_for_librarian = Library.objects.get(name="City Central Library")
    librarian = library_for_librarian.librarian
    print(f"- {librarian.name}")