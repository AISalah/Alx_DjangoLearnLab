
---

# Social Media API - Capstone Project

A robust RESTful API built with Django and Django REST Framework, featuring custom user authentication, token generation, and profile management.

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository (or navigate to project folder):**
   ```bash
   cd social_media_api
   ```

2. **Create and Activate a Virtual Environment:**
   - *Windows:*
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - *Mac/Linux:*
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install django djangorestframework pillow
   ```

4. **Database Setup:**
   Run migrations to set up the Custom User model and Auth Tokens.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```



## 👤 User Model Architecture

The project uses a **Custom User Model** (`accounts.CustomUser`) that extends Django's `AbstractUser`.

**Custom Fields:**
- `bio` (Text): A short description of the user.
- `profile_picture` (Image): Upload path: `/profile_pictures/`.
- `followers` (ManyToMany): A non-symmetrical relationship to other users.



## Authentication & Endpoints

Base URL: `http://127.0.0.1:8000/api/`

### 1. Register a New User
Creates a user and returns an authentication token immediately.

- **Endpoint:** `POST /register/`
- **Body (JSON):**
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "StrongPassword123!",
      "bio": "Slam!",
      "profile_picture": (optional file)
  }
  ```
- **Response:** Returns User data + `token`.

### 2. Login
Obtain an authentication token for an existing user.

- **Endpoint:** `POST /login/`
- **Body (JSON):**
  ```json
  {
      "username": "johndoe",
      "password": "StrongPassword123!"
  }

- **Response:**
  ```json
  {
      "token": "9dc29e561c6ab68d1b7d104e663381f372afed58"
  }


### 3. User Profile
View or update the logged-in user's details.

- **Endpoint:** `GET /profile/` or `PUT /profile/`
- **Headers Required:**
  - Key: `Authorization`
  - Value: `Token <your_token_string>`


## Content Management (Posts & Comments)

The API supports full CRUD operations for Posts and Comments.
**Note:** All write operations (Create, Update, Delete) require the `Authorization: Token <token>` header.

### 1. Posts

#### List & Search Posts
- **Endpoint:** `GET /posts/`
- **Filtering:** Use `?search=` to find posts by title or content.
- **Pagination:** Returns 10 results per page.
- **Example URL:** `http://127.0.0.1:8000/api/posts/?search=API&page=1`
- **Response:**
  ```json
  {
      "count": 5,
      "next": "http://.../page=2",
      "results": [
          {
              "id": 1,
              "author": "testuser",
              "title": "My First Post",
              "content": "Salam!",
              "created_at": "2023-10-27T10:00:00Z"
          }
      ]
  }

#### Create a Post
- **Endpoint:** `POST /posts/`
- **Body:**
  ```json
  {
      "title": "New Feature",
      "content": "just added filtering!"
  }


#### Edit/Delete a Post
- **Endpoint:** `PUT /posts/{id}/` or `DELETE /posts/{id}/`
- **Permission:** Only the **author** of the post can perform these actions.

### 2. Comments

#### Create a Comment
- **Endpoint:** `POST /comments/`
- **Body:**
  ```json
  {
      "post": 1,
      "content": "Great post!"
  }


#### List Comments
- **Endpoint:** `GET /comments/`
- **Response:** Lists all comments ordered by newest first.

### Task: Update `README.md`
Open your file and append this new section at the bottom (or integrate it into the existing sections).

##  Social Features & Feed

### User Model Updates
The `CustomUser` model has been updated to support relationships:
- **`following`**: A Many-to-Many field (symmetrical=False) allowing users to follow others.

### Endpoints

#### 1. Follow a User
Start following a specific user.
- **Endpoint:** `POST /follow/<id>/`
- **Headers:** `Authorization: Token <your_token>`
- **Response:**
  ```json
  {
      "message": "You are now following testuser2"
  }

#### 2. Unfollow a User
Stop following a specific user.
- **Endpoint:** `POST /unfollow/<id>/`
- **Headers:** `Authorization: Token <your_token>`
- **Response:**
  ```json
  {
      "message": "You have unfollowed testuser2"
  }


#### 3. User Feed
Retrieves a paginated list of posts *only* from authors the user follows.
- **Endpoint:** `GET /feed/`
- **Headers:** `Authorization: Token <your_token>`
- **Response:**
  ```json
  {
      "count": 5,
      "results": [
          {
              "id": 2,
              "author": "StarUser",
              "title": "Star Life",
              "content": "This post should appear in the feed!",
              ...
          }
      ]
  }