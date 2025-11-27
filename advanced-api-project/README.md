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

## 6.Advanced Features: Filtering, Searching, and Ordering

The `ListView` endpoint (`/api/books/`) supports robust query parameters to refine results.

### 6.1. Filtering
Filter the list by exact matches for specific fields.
- **Fields:** `title`, `author`, `publication_year`
- **Example:** Get books published in 1377:
  - GET /api/books/?publication_year=1377

**Example:** Get books by Author ID 1:
    GET /api/books/?author=1

### 6.2. Searching
Perform a fuzzy text search across book titles and author names.
- **Fields:** `title`, `author__name`
- **Example:** Search for "Animal":
```bash
 GET /api/books/?search=Animal
 ```
**Example: Search for a book by author**
```bash
GET http://127.0.0.1:8000/api/books/?search=Ibnkhaldun
```

### 6.3. Ordering
Sort the results by specific fields. Use a minus sign (`-`) for descending order.
- **Fields:** `title`, `publication_year`
- **Example:** Sort by newest books first:
  - GET /api/books/?ordering=-publication_year
- **Example:** Sort alphabetically by title:
  - GET /api/books/?ordering=title




## Testing

This project uses Django's built-in `unittest` framework combined with DRF's `APITestCase` to ensure API reliability.

### How to Run Tests
To execute all automated tests, run the following command in your terminal:
```bash
python manage.py test api
```
### Test Coverage
The testing suite (`api/test_views.py`) covers the following scenarios:

- **Authentication & Permissions:**
  - Verifies that unauthenticated users **cannot** create, update, or delete books (HTTP 403).
  - Verifies that authenticated users **can** perform these actions (HTTP 201/200/204).

- **CRUD Operations:**
  - Tests the full lifecycle of a Book object: Create -> Update -> Delete.
  - Verifies database integrity after each operation.

- **Filtering & Searching:**
  - **Filtering:** Tests that filtering by `publication_year` returns specific results.
  - **Searching:** Tests that the search bar correctly identifies books by title.

### Interpreting Results
- **OK:** All tests passed successfully.
- **FAILED:** One or more assertions failed. Check the error trace for details.