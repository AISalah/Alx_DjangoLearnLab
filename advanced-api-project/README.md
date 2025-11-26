# Advanced API Project: Book Review System

This project is a Django REST Framework API for managing a collection of books and authors. It features advanced serialization, nested relationships, and secure CRUD operations.

## Features

- **Advanced Serialization**: Handles nested Author-Book relationships.
- **Custom Validation**: Prevents books from being created with future publication dates.
- **Robust Filtering**: Allows searching and ordering of book lists.
- **Security**: Implements distinct permission levels for reading vs. modifying data.

---

## API Documentation

### 1. List All Books
- **URL:** `/api/books/`
- **Method:** `GET`
- **View:** `ListView`
- **Permissions:** `IsAuthenticatedOrReadOnly` (Public access allowed)
- **Features:**
  - **Filtering:** Supports searching by `title` and `author__name`.
    - *Example:* `/api/books/?search=Almukaddimah`
  - **Ordering:** Supports sorting by `title` and `publication_year`.
    - *Example:* `/api/books/?ordering=-publication_year` (Newest first)

### 2. Retrieve a Single Book
- **URL:** `/api/books/<id>/`
- **Method:** `GET`
- **View:** `DetailView`
- **Permissions:** `IsAuthenticatedOrReadOnly` (Public access allowed)
- **Description:** Returns detailed information about a specific book by its ID.

### 3. Create a New Book
- **URL:** `/api/books/create/`
- **Method:** `POST`
- **View:** `CreateView`
- **Permissions:** `IsAuthenticated` (Requires Login)
- **Custom Behavior:**
  - Uses `BookSerializer` to validate data.
  - **Validation Hook:** Automatically rejects any book with a `publication_year` in the future.

### 4. Update a Book
- **URL:** `/api/books/update/<id>/`
- **Method:** `PUT`, `PATCH`
- **View:** `UpdateView`
- **Permissions:** `IsAuthenticated` (Requires Login)
- **Description:** Modifies an existing book. Requires the user to be authenticated.

### 5. Delete a Book
- **URL:** `/api/books/delete/<id>/`
- **Method:** `DELETE`
- **View:** `DeleteView`
- **Permissions:** `IsAuthenticated` (Requires Login)
- **Description:** Permanently removes a book from the database.

---

## Testing & Usage

To test the API, you can use the built-in Browsable API or tools like Postman/cURL.

**Example: Search for a book by author**
```bash
GET http://127.0.0.1:8000/api/books/?search=Ibnkhaldun