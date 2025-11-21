from .serializers import BookSerializer
from .models import Book
from django.shortcuts import render
from rest_framework import generics

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

