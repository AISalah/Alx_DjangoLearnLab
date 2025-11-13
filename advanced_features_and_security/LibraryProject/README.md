# Book Management Permissions Setup

This document outlines the permission system used to control access to book management features in the `bookshelf` app.

### 1. Defining Custom Permissions

The custom permissions are defined directly within the `Book` model in the `bookshelf/models.py` file, inside the inner `Meta` class.

The following custom permissions have been created:
- `can_view`: Allows users to view the details of a book.
- `can_create`: Allows users to access the form and create a new book.
- `can_edit`: Allows users to edit the details of an existing book.
- `can_delete`: Allows users to delete a book.

### 2. Creating Roles with Groups

To assign these permissions to users, we use Django's built-in Group system. The intended setup is as follows:

1.  A group named **"Librarians"** is created in the Django admin panel.
2.  All of the book-related permissions ( `can_view`, `can_create`, etc.) are assigned to this "Librarians" group.
3.  Any user who should have these powers is then added as a member of the "Librarians" group.

### 3. Enforcing Permissions in Views

Access to the pages is restricted in `bookshelf/views.py` using the `@permission_required` decorator.

For example, the view that handles creating a book is protected like this:
`@permission_required('bookshelf.can_create', raise_exception=True))`

This ensures that only logged-in users who are part of a group with the `can_create` permission can access that page.