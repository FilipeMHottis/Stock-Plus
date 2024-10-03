# Service Layer

The service layer will be responsible for implementing the business logic related to user management, including permission verification and integration with the authentication layer (JWT). The service processes requests from the controller, applies business rules, and interacts with the data layer (models) for persistence.

---

## User

<details>

## Service Layer Functionalities

### 1. **User Creation**

- **Method**: `create_user(data: dict, current_user: User)`
- **Input**:
  - `data`: Dictionary containing the new user’s data (`name`, `username`, `email`, `password`, `role`).
  - `current_user`: The authenticated user, who must be an **admin**.
- **Business Rules**:
  - Only **admins** can create new users.
  - The new user must have a valid `role` (admin, supervisor, cashier).
  - Check for duplicate `email` or `username`.
- **Output**: Created user or permission/validation error.

### 2. **User Modification**

- **Method**: `update_user(user_id: int, data: dict, current_user: User)`
- **Input**:
  - `user_id`: ID of the user to be modified.
  - `data`: Dictionary containing the fields to be updated.
  - `current_user`: The authenticated user, who can be either an **admin** or a **supervisor**.
- **Business Rules**:
  - **Admins** can modify any user.
  - **Supervisors** can modify users with **cashier** or **supervisor** roles, but not **admin**.
  - **Cashiers** cannot modify their own profile or others.
  - Ensure that a role (`role`) cannot be escalated improperly (e.g., a supervisor changing their own role to admin).
- **Output**: Updated user or permission/validation error.

### 3. **User Deletion**

- **Method**: `delete_user(user_id: int, current_user: User)`
- **Input**:
  - `user_id`: ID of the user to be deleted.
  - `current_user`: The authenticated user, who can be either an **admin** or a **supervisor**.
- **Business Rules**:
  - **Admins** can delete any user.
  - **Supervisors** can only delete **cashiers** or **other supervisors**.
  - **Cashiers** are not allowed to delete users.
  - Ensure that **admins** cannot be deleted by **supervisors**.
- **Output**: Confirmation of deletion or permission error.

### 4. **User Retrieval**

- **Method**: `get_user(user_id: int, current_user: User)`
- **Input**:
  - `user_id`: ID of the user to be retrieved.
  - `current_user`: The authenticated user.
- **Business Rules**:
  - All users (admin, supervisor, cashier) can view other users' details.
- **Output**: Details of the requested user.

### 5. **User Listing**

- **Method**: `list_users(current_user: User)`
- **Input**:
  - `current_user`: The authenticated user.
- **Business Rules**:
  - All users (admin, supervisor, cashier) can list all users in the system.
- **Output**: List of users.

### 6. **Permission Verification**

- **Method**: `check_permissions(action: str, current_user: User, target_user: User = None)`
- **Input**:
  - `action`: The action the user is attempting to perform (create, update, delete, view).
  - `current_user`: The authenticated user trying to perform the action.
  - `target_user`: The user being targeted by the action (if applicable).
- **Business Rules**:
  - Verify whether the `current_user` has the appropriate permissions to execute the desired action on the `target_user`.
  - Permissions are determined by the `role` of the `current_user` and the system's established rules.
- **Output**: `True` (if permitted) or permission error.

</details>

---

## Validation and Security Layer

<details>

### 1. **Data Validation**

- Each service (creation, modification, etc.) must perform validation on the received data (e.g., `email`, `username`, `password`) before any database operation.
- Ensure that required fields are provided and that the formats are correct.

### 2. **JWT Protection**

- Implement JWT token validation for each service method.
- Check the user's role (`role`) within the token and apply corresponding permissions.

</details>

---

## Interaction with the Data Layer (Models)

<details>

- The service layer will interact with the **models** to create, update, and query user data.
- An ORM like SQLAlchemy or Peewee will be used to abstract database operations.
  - **Example**: `User.query.filter_by(id=user_id).first()` to fetch a user by ID.

</details>

## Errors and Exceptions

<details>

- The service layer must handle exceptions and return appropriate messages to the controller layer.
  - Example: "User not found", "Permission denied", "Invalid fields", etc.

- **Validation Error**: Return `ValidationError` with status code `422`.
- **Permission Error**: Return `PermissionError` with status code `403`.

</details>
