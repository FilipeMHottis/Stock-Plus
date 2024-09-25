# Model

This document describes the structure and attributes of each model in the sales platform.

---

## User Model

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

---

## Product Model

<details>

### 1. **Field Name**: `name`

- **Type**: `String`
- **Description**: The name of the product.
- **Validations**:
  - Required (cannot be null)
  - Maximum length: 255 characters.

### 2. **Field Name**: `description`

- **Type**: `String`
- **Description**: A description of the product.
- **Validations**:
  - Optional (can be null)
  - Maximum length: 500 characters.

### 3. **Field Name**: `price`

- **Type**: `Decimal`
- **Description**: The price of the product.
- **Validations**:
  - Required (cannot be null)
  - Maximum digits: 10
  - Decimal places: 2

### 4. **Field Name**: `stock`

- **Type**: `Integer`
- **Description**: The quantity of the product available in stock.
- **Validations**:
  - Required (cannot be null)
  - Default value: 0

### 5. **Field Name**: `barcode`

- **Type**: `String`
- **Description**: Optional barcode for the product.
- **Validations**:
  - Optional (can be null)
  - Maximum length: 50 characters.

### 6. **Field Name**: `custom_code`

- **Type**: `String`
- **Description**: A customizable identification code for the product.
- **Validations**:
  - Optional (can be null)
  - Maximum length: 20 characters.

### 7. **Field Name**: `image_url`

- **Type**: `String`
- **Description**: URL of the product image for frontend display.
- **Validations**:
  - Optional (can be null)

### 8. **Field Name**: `created_at`

- **Type**: `Datetime`
- **Description**: The date and time when the product was created.
- **Validations**:
  - Default value: Current date and time.

</details>

---

## Payment Method Model

<details>

### 1. **Field Name**: `method`

- **Type**: `String`
- **Description**: The name of the payment method.
- **Validations**:
  - Required (cannot be null)
  - Maximum length: 50 characters.
  - Must be unique.

### 2. **Field Name**: `description`

- **Type**: `String`
- **Description**: Optional description of the payment method.
- **Validations**:
  - Optional (can be null)
  - Maximum length: 255 characters.

</details>

---

## Sale Model

<details>

### 1. **Field Name**: `user_id`

- **Type**: `Foreign Key` (User)
- **Description**: The user who made the sale.
- **Validations**:
  - Required (cannot be null)

### 2. **Field Name**: `sale_date`

- **Type**: `Datetime`
- **Description**: The date and time when the sale occurred.
- **Validations**:
  - Default value: Current date and time.

### 3. **Field Name**: `payment_method_id`

- **Type**: `Foreign Key` (PaymentMethod)
- **Description**: The method of payment used for the sale.
- **Validations**:
  - Optional (can be null)

### 4. **Field Name**: `discount`

- **Type**: `Decimal`
- **Description**: The discount applied to the sale.
- **Validations**:
  - Optional (can be null)
  - Default value: `0`
  - Maximum digits: 10
  - Decimal places: 2

</details>

---

## Sale Product Model

<details>

### 1. **Field Name**: `sale_id`

- **Type**: `Foreign Key` (Sale)
- **Description**: The sale this product belongs to.
- **Validations**:
  - Required (cannot be null)

### 2. **Field Name**: `product_id`

- **Type**: `Foreign Key` (Product)
- **Description**: The product being sold.
- **Validations**:
  - Required (cannot be null)

### 3. **Field Name**: `quantity`

- **Type**: `Integer`
- **Description**: The quantity of the product sold in this sale.
- **Validations**:
  - Required (cannot be null)

</details>

---

### **Relationships between Tables**

1. **User - Sale**:
   - A user can have many sales (`One-to-Many`).
   - Each sale is made by one user.

2. **Sale - Payment Method**:
   - Each sale can have one payment method (`Many-to-One`).
   - A payment method can be used for many sales.

3. **Sale - Product (through SaleProduct)**:
   - A sale can have many products (`Many-to-Many`).
   - A product can be part of many sales.
   - The `SaleProduct` table acts as a join table that connects sales and products.
