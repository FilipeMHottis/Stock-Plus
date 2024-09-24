# Model

This document describes the structure and attributes of each model in the sales platform.

---

## User

<details>

### 1. **Field Name**: `name`

- **Type**: `String`
- **Description**: Full name of the user (vendor).
- **Validations**:
  - Required (cannot be null)
  - Maximum length: 255 characters.

### 2. **Field Name**: `username`

- **Type**: `String`
- **Description**: Unique username that will be used for login.
- **Validations**:
  - Required (cannot be null)
  - Must be unique
  - Maximum length: 50 characters.

### 3. **Field Name**: `email`

- **Type**: `String`
- **Description**: Unique email of the user for authentication and communication.
- **Validations**:
  - Required (cannot be null)
  - Must be unique
  - Maximum length: 100 characters.
  - Valid email format.

### 4. **Field Name**: `password_hash`

- **Type**: `String`
- **Description**: Encrypted password stored as a hash (bcrypt).
- **Validations**:
  - Required (cannot be null)
  - The password will be stored as a hash for security purposes.

### 5. **Field Name**: `role`

- **Type**: `String`
- **Description**: Defines the role, which can be "admin", "cashier", or "supervisor".
- **Validations**:
  - Required (cannot be null)
  - Default value: `cashier`
  - Maximum length: 20 characters.

### 6. **Field Name**: `is_active`

- **Type**: `Boolean`
- **Description**: Indicates whether the user is active on the platform.
- **Validations**:
  - Default value: `True`

### 7. **Field Name**: `created_at`

- **Type**: `Datetime`
- **Description**: The date and time when the user account was created.
- **Validations**:
  - Default value: Current date and time.

</details>
