from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author


class TestBookAPITests(APITestCase):
    def setUp(self):
        # 1. Create a test user (for login tests later)
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # 2. Create an Author
        self.author = Author.objects.create(name="Ibn Khaldun")

        # 3. Create a Book
        self.book = Book.objects.create(
            title="Almukaddimah",
            publication_year=1377,
            author=self.author
        )

        # 4. The tested URL
        self.list_url = '/api/books/'

    def test_create_book_authenticated(self):
        """Test that a logged-in user can create a book"""
        # 1. Log in the user in setUp
        self.client.login(username='testuser', password='testpassword')

        # 2. Prepare the new book data
        data = {
            'title': '1984',
            'publication_year': 1945,
            'author': self.author.id
        }

        # 3. Send a POST request
        response = self.client.post('/api/books/create/', data)

        # 4. Check the result
        # HTTP 201 means "Created"
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the book is actually in the database
        self.assertEqual(Book.objects.get(title='1984').title, '1984')

    def test_create_book_unauthenticated(self):
        """Test that a user NOT logged in cannot create a book"""
        # 1. Prepare data
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2025,
            'author': self.author.id
        }

        # 2. Send POST request (Without logging in!)
        response = self.client.post('/api/books/create/', data)

        # 3. Check the result
        # HTTP 403 means "Forbidden" (or 401 Unauthorized)
        # Because we used IsAuthenticated, it should block us.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test that a logged-in user can update a book"""
        self.client.login(username='testuser', password='testpassword')

        # 1. Change the year from 1377 to 2000
        data = {
            'title': 'Almukaddimah Updated',
            'publication_year': 2000,
            'author': self.author.id
        }

        # 2. Send PUT request to the update URL
        response = self.client.put(f'/api/books/update/{self.book.id}/', data)

        # 3. Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 4. Refresh the book from DB and check the title
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Almukaddimah Updated')

    def test_delete_book(self):
        """Test that a logged-in user can delete a book"""
        self.client.login(username='testuser', password='testpassword')

        # 1. Send DELETE request
        response = self.client.delete(f'/api/books/delete/{self.book.id}/')

        # 2. Check status (204 No Content is standard for delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # 3. Verify it is gone
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering by publication year"""
        # 1. Request books from the correct year (1377)
        response = self.client.get(self.list_url + '?publication_year=1377')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should find 1 book
        self.assertEqual(response.data[0]['title'], 'Almukaddimah')

        # 2. Request books from a wrong year (2022)
        response = self.client.get(self.list_url + '?publication_year=2022')
        self.assertEqual(len(response.data), 0)  # Should be empty

    def test_search_books(self):
        """Test searching by title and author"""
        # 1. Search for part of the title "Almukaddimah"
        response = self.client.get(self.list_url + '?search=Almukaddimah')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # 2. Search for something that doesn't exist "Harry"
        response = self.client.get(self.list_url + '?search=Harry')
        self.assertEqual(len(response.data), 0)
