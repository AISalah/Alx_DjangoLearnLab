from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# 1. ListView: Retrieve all books
class ListView(generics.ListAPIView):
    """
        Retrieves a list of all books.

        Features:
        - **Filtering:** Filter by title, author ID, or publication year.
          (e.g., ?author=1&publication_year=2023)
        - **Searching:** Search by book title or author name.
          (e.g., ?search=Rowling)
        - **Ordering:** Sort results by title or publication year.
          (e.g., ?ordering=-publication_year)

        Permissions:
        - Read-only access for unauthenticated users.
        """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    # Enable Search and Ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year']

    filterset_fields = ['title', 'author', 'publication_year']

    # Allow anyone to read
    permission_classes = [IsAuthenticatedOrReadOnly]

# 2. DetailView: Retrieve a single book
class DetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.

    Features:
    - Looks up a specific book using the primary key (pk) from the URL.
    - Permissions: Allowed for everyone (Read-Only for unauthenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    # Allow anyone to read
    permission_classes = [IsAuthenticatedOrReadOnly]

# 3. CreateView: Add a new book
class CreateView(generics.CreateAPIView):
    """
        View to create a new book.

        Features:
        - Handles POST requests to add new Book instances.
        - specific behavior: Validates data using BookSerializer (e.g., future dates check).
        - Permissions: Restricted to authenticated users only.
        """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Lock this down! Only logged-in users.
    permission_classes = [IsAuthenticated]

# 4. UpdateView: Modify an existing book
class UpdateView(generics.UpdateAPIView):
    """
        View to update an existing book.

        Features:
        - Handles PUT and PATCH requests to modify Book instances.
        - Permissions: Restricted to authenticated users only.
        """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lock view
    permission_classes = [IsAuthenticated]

# 5. DeleteView: Remove a book
class DeleteView(generics.DestroyAPIView):
    """
        View to delete a book.

        Features:
        - Handles DELETE requests to remove Book instances.
        - Permissions: Restricted to authenticated users only.
        """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # lock view
    permission_classes = [IsAuthenticated]