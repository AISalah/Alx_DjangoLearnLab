from .models import Author, Book, Library, Librarian

def run_queries():
    print("Creating sample data...")
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="Ibn Khaldun")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Al-Mukaddimah", author=author2)

    library1 = Library.objects.create(name="Books Hub")
    library1.books.add(book1, book3)

    librarian1 = Librarian.objects.create(name="Books keeper", library=library1)
    print("Sample data created.\n")

    # 1. Query all books by a specific author (George Orwell)
    print("1. Books by George Orwell:")
    orwell_books = Book.objects.filter(author__name="George Orwell")
    for book in orwell_books:
        print(f"- {book.title}")
    print("-" * 20)

    # 2. List all books in a library
    print("2. Books in Books Hub:")
    books_hub = library1.books.all()
    for book in  books_hub:
        print(f"- {book.title}")
    print("-" * 20)

    # 3. Retrieve the librarian for a library
    print("3. Librarian for Books Hub:")
    librarian_name = library1.librarian.name
    print(f"- {librarian_name}")
    print("-" * 20)