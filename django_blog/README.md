# Django Blog Authentication System Documentation

## 1. Overview
This module handles the security and user management for the Django Blog. It allows users to create accounts, securely log in and out, and manage their personal profile information. The system leverages Django's built-in `auth` framework for robust security while implementing custom views for better user experience.

## 2. Technical Components

### A. Registration
*   **View:** Custom function-based view in `blog/views.py`.
*   **Form:** `CustomUserCreationForm` (extends Django's default form to include Email).
*   **Logic:**
    *   Validates username uniqueness and password strength.
    *   Upon success, the user is **automatically logged in** and redirected to the Home page.

### B. Login & Logout
*   **Views:** Uses Django's built-in `LoginView` and `LogoutView`.
*   **Templates:** `blog/login.html` and `blog/logout.html`.
*   **Logic:**
    *   **Login:** valid credentials create a session ID stored in the browser cookies.
    *   **Logout:** Destroys the session ID, effectively logging the user out.

### C. Profile Management
*   **View:** `profile` function in `blog/views.py`.
*   **Security:** Protected by the `@login_required` decorator.
*   **Form:** `UserUpdateForm` (allows updating Username and Email).
*   **Logic:**
    *   **GET Request:** Pre-fills the form with the current logged-in user's data (`instance=request.user`).
    *   **POST Request:** Validates new input and saves changes to the User model.



## 3. User Interaction & Workflows

### Scenario 1: New User Sign Up
1.  User navigates to `/register/`.
2.  User enters a Username, Email, and Password (twice).
3.  **System Action:** Checks if username exists. Checks password complexity.
4.  **Result:** User account is created in the database and user is redirected to the Dashboard.

### Scenario 2: Updating Profile
1.  Logged-in user navigates to `/profile/`.
2.  User sees their current email address in the box.
3.  User changes the email and clicks "Update".
4.  **System Action:** Database is updated with the new email. Page reloads to show the confirmation.

### Scenario 3: Unauthorized Access
1.  A user who is **not** logged in tries to visit `/profile/`.
2.  **System Action:** The `@login_required` decorator intercepts the request.
3.  **Result:** User is immediately redirected to the Login page (`/login/?next=/profile/`).


## Blog Post Management System

This module enables full CRUD (Create, Read, Update, Delete) functionality for blog posts.

### Features & URLs
*   **View All Posts:** `/posts/` - Displays a paginated list of all posts (latest first). Content is truncated to 10 words for brevity.
*   **Read Post:** `/posts/<id>/` - Displays the full content of a single post.
*   **Create Post:** `/posts/new/` - Shows a form to write a new post.
*   **Edit Post:** `/posts/<id>/edit/` - Allows authors to modify their existing posts.
*   **Delete Post:** `/posts/<id>/delete/` - Asks for confirmation before permanently removing a post.

### Permissions & Security
The system enforces strict access control using Django Mixins:
1.  **Public Access:** Anyone can view the List and Detail pages.
2.  **Authenticated Access:** Only logged-in users can access the Create page (`LoginRequiredMixin`).
3.  **Author-Only Access:** The Edit and Delete pages use `UserPassesTestMixin` to ensure that **only the original author** can modify or delete their post. Attempts by others result in a 403 Forbidden error.

### Technical Implementation
*   **Automatic Authoring:** The `CreateView` is customized to automatically assign the currently logged-in user as the `author` of the post, removing the need for a manual selection field.
*   **Pagination:** The post list is configured to paginate results (currently set to 5 posts per page) to optimize performance.

## Authentication & User Management

The project includes a full user authentication system allowing for secure access control.

### Features
*   **Registration:** `/register/` - Users can create an account using a custom form that includes email validation.
*   **Login:** `/login/` - Standard Django login view.
*   **Logout:** `/logout/` - Secure logout (POST request required) to protect against CSRF attacks.
*   **Profile:** `/profile/` - Authenticated users can update their username, email, and upload a profile picture.

### Security Implementation
*   **Passwords:** Stored using PBKDF2 password hashing (standard Django security).
*   **Access Control:** 
    *   `LoginRequiredMixin` is used on Create/Update/Delete views to prevent anonymous access.
    *   `UserPassesTestMixin` ensures users can only edit/delete their *own* content.

### Testing Instructions
1.  **Register:** Create a new user at `/register/`. You should be redirected to the home page.
2.  **Login/Logout:** Test the Login and Logout links in the navigation bar.
3.  **Profile:** Navigate to `/profile/` to upload a custom avatar and verify it displays correctly.