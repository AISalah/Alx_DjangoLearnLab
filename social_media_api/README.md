
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

---

## 👤 User Model Architecture

The project uses a **Custom User Model** (`accounts.CustomUser`) that extends Django's `AbstractUser`.

**Custom Fields:**
- `bio` (Text): A short description of the user.
- `profile_picture` (Image): Upload path: `/profile_pictures/`.
- `followers` (ManyToMany): A non-symmetrical relationship to other users.

---

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
  ```
- **Response:**
  ```json
  {
      "token": "9dc29e561c6ab68d1b7d104e663381f372afed58"
  }
  ```

### 3. User Profile
View or update the logged-in user's details.

- **Endpoint:** `GET /profile/` or `PUT /profile/`
- **Headers Required:**
  - Key: `Authorization`
  - Value: `Token <your_token_string>`
