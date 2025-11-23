from .serializers import BookSerializer
from .models import Book
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions



# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # This ViewSet provides the standard CRUD operations for the Book model.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    # PERMISSION_CLASSES CONFIGURATION:
    # We restrict access so that only authenticated users can interact with this API.
    # Unauthenticated requests will receive a 401 Unauthorized response.
    permission_classes = [permissions.IsAuthenticated]


