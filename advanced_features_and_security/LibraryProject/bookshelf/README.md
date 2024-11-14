# Django Permission Setup

### Model Permissions
The `Book` model has four custom permissions:
- `can_view`: Can view books.
- `can_create`: Can create new books.
- `can_edit`: Can edit existing books.
- `can_delete`: Can delete books.

These permissions are defined in the `Meta` class of the `Book` model.

### Groups and Permissions
- **Editors**: Can create and edit articles (`can_create`, `can_edit`, `can_view`).
- **Viewers**: Can view articles (`can_view`).
- **Admins**: Can create, view, edit, and delete articles (`can_create`, `can_view`, `can_edit`, `can_delete`).

### Views Protection
- `@permission_required('bookshelf.can_create')`: Protects views so that only users with the correct permissions can perform actions like creating, editing, or deleting books.

### Testing
- Users should be assigned to the appropriate groups.
- Verify that each user can only perform actions they have permissions for.
