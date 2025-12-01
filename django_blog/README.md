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

