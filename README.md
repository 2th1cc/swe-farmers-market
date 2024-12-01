# Farmer Market System

Nazarbayev University
SOFTWARE ENGINEERING CSCI 361

## Team Members:

- Lazzat Zhengissova
- Akmaral Ayazbay
- Yeldos Nurpeissov
- Azimzhan Abdrakhmanov
- Zeindi Adakhajiyev
- Yezhan Tugralin
---
## Contents

- [Technology Stack](#technology-stack)
- [Diagrams](#diagrams)
  - [Class Diagram](#class-diagram)
  - [Component Diagram](#component-diagram)
  - [Use Case Diagram](#use-case-diagram)
  - [Activity Diagram](#activity-diagram)
  - [ER Diagram](#er-diagram)
  - [Database](#database)
- [Software Details](#software-details)
  - [User Registration and Authentification](#user-registration-and-authentification)
  - [Farmer Interface](#farmer-interface)
  - [Buyer Interface](#buyer-interface)
  - [Admin Interface](#admin-interface)

---

## Technology Stack

The Farmers Market System is a specialized platform developed to improve the interaction between farmers and buyers, providing a streamlined experience for managing agricultural products. Each technology used in the system was carefully chosen to ensure efficiency, security, and ease of use.

For the user interface, we utilized Django's templating engine combined with standard web technologies like HTML, CSS, and JavaScript. This enabled us to design a clean, responsive, and easy-to-navigate interface tailored to user needs.

For the mobile stack, the system can be expanded using Flutter, a cross-platform framework known for its performance and flexibility. Flutter would allow the development of a single mobile application for both iOS and Android, maintaining a consistent user experience across devices.

On the backend, Django was selected as the primary framework due to its robust capabilities for handling complex operations. It simplifies tasks such as database interactions, user authentication, and API creation. To expose functionalities through APIs, Django REST Framework (DRF) was employed, which offers tools to build secure and efficient endpoints.

SQLite3 serves as the database for this project. Its lightweight nature and simplicity make it an excellent choice for the scale of this system. The database manages all essential entities, such as products, orders, users, and notifications, in a structured manner.

Additional functionality was incorporated using tools like Pillow, which enables image handling and optimization. Filtering and search functionalities were enhanced through Django Filters, allowing users to locate products or information quickly.

Together, this stack—Django for backend operations, SQLite3 for data storage, and standard frontend tools—creates a system designed to meet the needs of the farming community. The result is a reliable, functional platform that connects farmers and buyers effectively.

---

## Diagrams

To better understand how a system works and simplify further planning we have created four UML diagrams: Class, Component, Use Case and Activity  diagrams. These diagrams are presented below.

---
### Class Diagram

<img src="https://github.com/user-attachments/assets/3ba7b878-a7a3-4274-9739-dd755116fbea" width="650">

This UML diagram outlines the roles and interactions within the Farmer Market System:

- **Users**: All users, including Buyers, Farmers, and Administrators, have access to basic registration, login, and profile management.
- **Buyers**: Buyers can browse products, add items to their cart, place and track orders, and view their purchase history. They can also communicate directly with Farmers via the chat module.
- **Farmers**: Farmers manage product listings, inventory, and sales. They fulfill orders placed by Buyers and update order statuses. Farmers also generate reports to track sales and inventory.
- **Orders**: Orders represent transactions between Buyers and Farmers, linking products and purchases, including delivery details and order status.
- **Reports**: Both Buyers and Farmers can generate reports, including sales for Farmers and purchase history for Buyers.
- **Administrators**: Administrators manage users and global system settings, ensuring the platform operates smoothly and overseeing user activities.
- **Chat**: The chat feature enables direct communication between Buyers and Farmers, facilitating questions and discussions about products.

These interactions and roles ensure smooth functionality, data management, and communication within the platform.

---
### Component Diagram

<img src="https://github.com/user-attachments/assets/ab7d396c-f1f6-4c61-a75b-29daec5061c7" width="650">

This Component Diagram provides a high-level view of the Farmer's Market platform and how its various components interact:

#### **Frontend API**: Acts as a bridge between the mobile and web applications and the backend services.
- **Mobile Application**: A user-friendly app for consumers and farmers to interact with the platform, accessible on the go.
- **Web Application**: A browser-based interface offering similar functionality as the mobile app, designed for desktop users.
#### **API Gateway**: A centralized entry point that routes incoming requests from the frontend apps to the appropriate backend services. It handles security, load balancing, and rate limiting.
#### **Backend Services**: Comprises multiple modular services for specific tasks:
  1. **Product Management Service**: Manages product listings, interacting with the Product Data database.
  2. **Order Management Service**: Manages the entire order lifecycle, integrates with external payment and logistics services, and stores data in the Order Data database.
  3. **Chat Service**: Facilitates direct communication between buyers and farmers, storing chat history in the Chat Data database.
  4. **Notification Service**: Sends real-time notifications to users about order updates or new messages.
  5. **Authentication Service**: Handles user authentication and authorization, working with the User Data database.
  6. **Reporting and Analytics Service**: Generates reports on user behavior, sales data, and platform performance, storing results in the Sales Data database.
  7. **Search Service**: Helps users quickly find products and services based on data.
#### **Databases**: Various databases store data specific to each service:
  - **Product Data**: Stores product listings.
  - **User Data**: Stores user profiles and authentication details.
  - **Order Data**: Stores information on orders and their status.
  - **Chat Data**: Stores chat histories.
  - **Sales Data**: Stores transactional data for reporting.
#### **External APIs**: Integrates with third-party services:
1. **Payment Gateway**: Facilitates secure payment processing between buyers and farmers.
2. **Logistics Provider API**: Manages shipping logistics and order tracking, ensuring timely deliveries.

This architecture ensures modularity, scalability, and effective interaction between various services, making the system efficient and user-friendly.

---
### Use Case Diagram

<img src="https://github.com/user-attachments/assets/f4199348-8ea4-47ae-beb5-ea51f5820cd8" width="650">

This use case diagram focuses on enhancing the Farmer's Market System, streamlining interactions and responsibilities between users:

- **Farmer Product Management**: Farmers can list, update, and manage their products, track inventory, and generate sales reports.
- **Buyer Interaction**: Buyers can register, log in, manage profiles, negotiate prices, and track orders.
- **Order Tracking**: Both farmers and buyers can track the status of orders, ensuring timely delivery and order fulfillment.
- **Admin Oversight**: Admins are responsible for monitoring system functionality, managing users, and overseeing platform performance.
- **Logistics and Delivery**: The logistics provider ensures smooth delivery by managing shipping and tracking product deliveries.
- **Payment Processing**: The Payment Gateway securely handles transactions between buyers and farmers, ensuring safe and timely payments.

---
### Activity Diagram

<img src="https://github.com/user-attachments/assets/b35c36f3-0d7f-4843-815f-a6ab305f966a" width="650">

The activity diagram illustrates the entire process flow in the Farmer's Market System, detailing the tasks performed by each entity:

- User: The user initiates the process by registering and verifying their account. Once verified, they log in, receive notifications, and interact with the platform through the dashboard. If needed, their account may be temporarily locked after multiple failed login attempts.
- Farmer: The farmer manages their profile and product listings after logging in. They update product details, inventory, and generate reports on sales and offers. The farmer’s activities revolve around product management and interacting with potential buyers.
- Buyer: The buyer searches for products, adds them to their cart, and proceeds with payment. Once payment is processed, they can track their order status and generate offers or reports related to their buying activities.
- System: The system interacts with multiple databases, validating data and confirming actions. It ensures smooth operation by sending notifications, confirming actions like orders and trades, and keeping all entities informed.
- Error Handling: The system checks for validation and error recovery throughout the process, ensuring that login and verification steps are correctly handled.

Overall, this diagram shows the complete cycle of operations, from registration to order tracking and reporting, providing a seamless experience for all actors involved in the system.

---
### ER Diagram 

<img src="https://github.com/user-attachments/assets/d84c3cdd-6589-4c26-ad01-15254f2cae93" width="650">


The diagrams helped guide the design and implementation of the database and system by providing a clear, visual representation of the relationships, attributes, and structure.
### Database

#### Entities and Attributes

##### 1.1. `auth_user`
**Attributes:**
- `id` (Primary Key)
- `password` (hashed password)
- `last_login` (datetime of the last login)
- `is_superuser` (boolean flag)
- `username` (unique, username of the user)
- `first_name`, `last_name` (name fields)
- `email` (email address)
- `is_staff`, `is_active` (boolean flags for permissions)
- `date_joined` (registration date)

**Purpose:** Represents standard Django users.

**Relationships:**
- Links to groups (`auth_user_groups`).
- Links to permissions (`auth_user_user_permissions`).

##### 1.2. `users_customuser`
**Attributes:**
- Similar to `auth_user` but adds:
  - `user_type` (integer, indicating the type of user: Farmer or Buyer)

**Relationships:**
- Extends `auth_user` functionality for custom roles (Farmer and Buyer).
- Links to groups (`users_customuser_groups`) and permissions (`users_customuser_user_permissions`).

##### 1.3. `users_farmer`
**Attributes:**
- `id` (Primary Key)
- `phone`, `registration_date`
- `is_approved` (boolean: farmer approval status)
- `rejection_feedback` (text: reasons if not approved)
- `farm_name`, `farm_location`
- `farm_size` (optional, size of the farm)
- `soil_type` (integer: a type representing soil category)

**Relationships:**
- Links to a single user in `users_customuser` (`user_id`, 1-to-1).
- Represents additional attributes specific to farmers.

##### 1.4. `users_buyer`
**Attributes:**
- `id` (Primary Key)
- `phone`, `registration_date`, `address`
- `default_delivery_method_id` (optional, references delivery methods)

**Relationships:**
- Links to a single user in `users_customuser` (`user_id`, 1-to-1).
- Represents additional attributes specific to buyers.


##### 1.5. `products_product`
**Attributes:**
- `id` (Primary Key)
- `name`, `category`, `description`
- `price` (decimal), `quantity` (integer)
- `is_out_of_stock` (boolean: availability status)

**Relationships:**
- Linked to a user (likely a Farmer) via `user_id` (1-to-Many).
- Products can have multiple images (`products_productimage`).
- Products can generate notifications (`products_lowstocknotification`).


##### 1.6. `products_productimage`
**Attributes:**
- `id` (Primary Key)
- `image` (file path)

**Relationships:**
- Linked to a product (`product_id`, 1-to-Many).


##### 1.7. `products_lowstocknotification`
**Attributes:**
- `id` (Primary Key)
- `created_at` (timestamp), `is_read` (boolean)

**Relationships:**
- Linked to a Farmer (`farmer_id`, 1-to-Many).
- Linked to a product (`product_id`, 1-to-Many).


##### 1.8. `orders_deliverymethod`
**Attributes:**
- `id` (Primary Key)
- `name`, `description`, `type`

**Relationships:**
- Linked optionally to buyers as their default delivery method.


##### 1.9. `django_admin_log`, `auth_*`, and `django_*` tables
**Purpose:** Support Django’s admin framework, authentication, and logging.

**Attributes:**
- Standard fields for logs, permissions, and sessions.



#### Relationships and Cardinalities

##### 2.1. User Relationships

###### `auth_user` and `auth_user_groups`
- **Cardinality:** Many-to-Many (users can belong to multiple groups).
- **Implemented via:** `auth_user_groups` table.

###### `auth_user` and `auth_user_user_permissions`
- **Cardinality:** Many-to-Many (users can have multiple permissions).
- **Implemented via:** `auth_user_user_permissions` table.

###### `users_customuser` and `users_farmer` / `users_buyer`
- **Cardinality:** One-to-One (a user can only be a Farmer or Buyer).
- **Ensured via:** `user_id` foreign key.


##### 2.2. Product Relationships

###### `users_customuser` (Farmers) and `products_product`
- **Cardinality:** One-to-Many (a Farmer can sell multiple products).

###### `products_product` and `products_productimage`
- **Cardinality:** One-to-Many (a product can have multiple images).

###### `products_product` and `products_lowstocknotification`
- **Cardinality:** One-to-Many (a product can trigger multiple notifications).

##### 2.3. Order Relationships

###### `users_buyer` and `orders_deliverymethod`
- **Cardinality:** One-to-One or One-to-Many (a Buyer can have a default delivery method).


#### Notable Constraints

##### 3.1. Uniqueness Constraints
- Users (`username`, `email` in `auth_user` and `users_customuser`).
- Groups and permissions (unique indices in `auth_group`, `auth_permission`).

##### 3.2. Foreign Key Constraints
- Used extensively to maintain referential integrity between related tables (e.g., products, farmers, buyers).



#### **SQLite3 Schema**

This schema reflects a Django-based system for managing farmers, buyers, and products in a farmer market system. Each role (Farmer or Buyer) extends the base users_customuser and interacts with products, orders, and delivery methods. The use of Many-to-Many relationships for permissions and groups enhances flexibility for user management.

```sql
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE TABLE IF NOT EXISTS "farmer_app_test" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "one" varchar(255) NOT NULL);
CREATE TABLE IF NOT EXISTS "orders_deliverymethod" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE, "description" text NULL, "type" varchar(20) NOT NULL);
CREATE TABLE IF NOT EXISTS "products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "category" varchar(10) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "quantity" integer NOT NULL, "is_out_of_stock" bool NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "products_lowstocknotification" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "is_read" bool NOT NULL, "farmer_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "products_productimage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "products_product_user_id_e04f062e" ON "products_product" ("user_id");
CREATE INDEX "products_lowstocknotification_farmer_id_aac91bc6" ON "products_lowstocknotification" ("farmer_id");
CREATE INDEX "products_lowstocknotification_product_id_850eec11" ON "products_lowstocknotification" ("product_id");
CREATE INDEX "products_productimage_product_id_e747596a" ON "products_productimage" ("product_id");
CREATE TABLE IF NOT EXISTS "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "domain" varchar(100) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "user_type" smallint unsigned NOT NULL CHECK ("user_type" >= 0), "email" varchar(254) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_customuser_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_customuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_buyer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone" varchar(15) NOT NULL, "registration_date" date NOT NULL, "address" varchar(255) NOT NULL, "default_delivery_method_id" bigint NULL REFERENCES "orders_deliverymethod" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL UNIQUE REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_farmer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone" varchar(15) NOT NULL, "registration_date" date NOT NULL, "is_approved" bool NOT NULL, "rejection_feedback" text NULL, "farm_name" varchar(255) NULL, "farm_location" varchar(255) NULL, "farm_size" varchar(100) NULL, "soil_type" integer unsigned NOT NULL CHECK ("soil_type" >= 0), "user_id" bigint NOT NULL UNIQUE REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "users_customuser_groups_customuser_id_group_id_76b619e3_uniq" ON "users_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "users_customuser_groups_customuser_id_958147bf" ON "users_customuser_groups" ("customuser_id");
CREATE INDEX "users_customuser_groups_group_id_01390b14" ON "users_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "users_customuser_user_permissions_customuser_id_permission_id_7a7debf6_uniq" ON "users_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "users_customuser_user_permissions_customuser_id_5771478b" ON "users_customuser_user_permissions" ("customuser_id");
CREATE INDEX "users_customuser_user_permissions_permission_id_baaa2f74" ON "users_customuser_user_permissions" ("permission_id");
CREATE INDEX "users_buyer_default_delivery_method_id_623a5395" ON "users_buyer" ("default_delivery_method_id");
CREATE TABLE IF NOT EXISTS "authtoken_token" ("key" varchar(40) NOT NULL PRIMARY KEY, "created" datetime NOT NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
```

#### Filling database with test data

##### Insert Data into `users_customuser` Table
```sql
INSERT INTO users_customuser (password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, user_type, email)
VALUES 
('password1', '2024-12-01 12:00:00', 1, 'superadmin', 'Super', 'Admin', 1, 1, '2024-12-01 10:00:00', 1, 'superadmin@example.com'),
('password2', NULL, 0, 'farmer_user1', 'John', 'Doe', 0, 1, '2024-12-01 11:00:00', 2, 'farmer1@example.com'),
('password3', '2024-12-02 09:30:00', 0, 'buyer_user1', 'Jane', 'Smith', 0, 1, '2024-12-01 11:30:00', 3, 'buyer1@example.com'),
('password4', NULL, 0, 'farmer_user2', 'Robert', 'Taylor', 0, 1, '2024-12-01 12:00:00', 2, 'farmer2@example.com'),
('password5', '2024-12-02 09:00:00', 0, 'buyer_user2', 'Alice', 'Brown', 0, 1, '2024-12-01 12:30:00', 3, 'buyer2@example.com');
```

![image](https://github.com/user-attachments/assets/8da78501-f0d5-416f-8087-187fbebf21ee)

##### Insert Data into `users_farmer` Table
```sql
INSERT INTO users_farmer (phone, registration_date, is_approved, rejection_feedback, farm_name, farm_location, farm_size, soil_type, user_id)
VALUES
('123-456-7890', '2024-12-01', 1, NULL, 'Sunny Farms', '123 Farm Road', '50 acres', 1, 2),
('987-654-3210', '2024-12-02', 0, 'Missing Documents', 'Rainy Meadows', '456 Field Lane', '20 acres', 2, 4);
```

![image](https://github.com/user-attachments/assets/2de10037-5ab2-4bed-8ac3-d54893803caf)

##### Insert Data into `users_buyer` Table
```sql
INSERT INTO users_buyer (phone, registration_date, address, default_delivery_method_id, user_id)
VALUES
('555-123-4567', '2024-12-01', '123 Market Street', NULL, 3),
('555-765-4321', '2024-12-02', '456 Shopping Avenue', NULL, 5);
```
![image](https://github.com/user-attachments/assets/3b43e46c-9872-42bb-8229-6c1cb5788018)


##### Insert Data into `orders_deliverymethod` Table
```sql
INSERT INTO orders_deliverymethod (name, description, type)
VALUES
('Courier', 'Delivery via courier service', 'Express'),
('Pick-Up', 'Customer pick-up from the farm', 'Standard'),
('Postal', 'Delivery through the postal system', 'Economy'),
('Drone', 'Automated drone delivery', 'Innovative'),
('Bulk Transport', 'Bulk delivery for large orders', 'Specialized');
```

![image](https://github.com/user-attachments/assets/c3f8889e-c45e-4abd-bf85-5047e1debde1)



##### Insert Data into `products_product` Table
```sql
INSERT INTO products_product (name, category, description, price, quantity, is_out_of_stock, user_id)
VALUES
('Organic Apples', 'Fruit', 'Freshly picked organic apples', 2.50, 100, 0, 2),
('Free Range Eggs', 'Poultry', 'Dozen of free range eggs', 4.00, 50, 0, 2),
('Whole Wheat Flour', 'Grain', 'Organic whole wheat flour', 3.00, 30, 0, 4),
('Honey', 'Sweetener', 'Raw natural honey', 10.00, 25, 0, 2),
('Goat Milk', 'Dairy', 'Fresh goat milk from our farm', 5.00, 0, 1, 4);

```

![image](https://github.com/user-attachments/assets/ccf88095-f01c-41ea-8dd9-8c04302d6c73)



As you can see by the pictures all of the insert queries work properly.

#### Queries to Test the Schema
1. Retrieve all farmers and their farm details:
```sql
SELECT u.username, f.farm_name, f.farm_location, f.farm_size
FROM users_farmer f
JOIN users_customuser u ON f.user_id = u.id;
```
![image](https://github.com/user-attachments/assets/447c8995-135a-4459-bb83-5c8bb4f4277f)

2. Retrieve all products and their stock status:
```sql
SELECT p.name, p.category, p.price, p.quantity, p.is_out_of_stock
FROM products_product p;
```
![image](https://github.com/user-attachments/assets/2aff0827-892d-4099-9df2-930a6314e1d7)

3. Select Rows with a Condition
```sql
SELECT * FROM users_customuser WHERE is_active = 1;
```
![image](https://github.com/user-attachments/assets/9821f60c-474c-48e6-8788-c25282140682)


4. Join Tables
```sql
SELECT 
    u.username, u.email, f.farm_name, f.farm_location 
FROM 
    users_customuser u
JOIN 
    users_farmer f ON u.id = f.user_id;
```
![image](https://github.com/user-attachments/assets/ee418526-a972-43c8-955c-8fb46c2691d9)


5. Aggregate Functions
```sql
SELECT COUNT(*) AS farmer_count FROM users_farmer;
```
![image](https://github.com/user-attachments/assets/c4ee00d2-cef4-4fd7-93f8-158f058c7a9b)

6. Group By with Aggregates
```sql
SELECT 
    type, COUNT(*) AS method_count 
FROM 
    orders_deliverymethod 
GROUP BY 
    type;

```
![image](https://github.com/user-attachments/assets/21f1b4ec-dd50-4de6-9381-f0d6c4856104)

7. Order By
```sql
SELECT 
    name, price 
FROM 
    products_product 
ORDER BY 
    price DESC;
```
![image](https://github.com/user-attachments/assets/1a018a50-0b08-4b12-b0c5-96169c2e55b4)

8. Inner Join Across Multiple Tables
```sql
SELECT 
    p.name AS product_name, p.price, f.farm_name, f.farm_location 
FROM 
    products_product p
JOIN 
    users_farmer f ON p.user_id = f.user_id;

```
![image](https://github.com/user-attachments/assets/8a13cd51-195e-4d17-8a02-6d8690195924)

9. Conditional Aggregates
```sql
SELECT 
    SUM(CASE WHEN is_out_of_stock = 0 THEN 1 ELSE 0 END) AS in_stock,
    SUM(CASE WHEN is_out_of_stock = 1 THEN 1 ELSE 0 END) AS out_of_stock
FROM 
    products_product;

```
![image](https://github.com/user-attachments/assets/766ec135-e64f-4455-a959-9e93c6330993)

10. Union
```sql
SELECT 
    phone 
FROM 
    users_farmer
UNION
SELECT 
    phone 
FROM 
    users_buyer;
```
![image](https://github.com/user-attachments/assets/e4f77a83-1b44-469d-8d57-b1ab3af6184a)


The database testing confirmed a functional design for managing users, farmers, buyers, products, and delivery methods. Queries for inserting, retrieving, and joining data worked well, with accurate results and smooth execution. Optional fields provided flexibility, and the schema handled test scenarios effectively. While the database is ready for use, further optimization and security enhancements would improve performance and scalability.


---

## Software Details
  
### User Registration and Authentification
Testing API Endpoints
#### Farmer Registration  
1. **Success**  
   <img src="https://github.com/user-attachments/assets/3954cc3e-9f1a-45ce-9d32-f57e4e7e08ae" width="400">  

2. **No Email**  
   <img src="https://github.com/user-attachments/assets/15a01dda-a50b-47d2-822a-67e38a637955" width="400">  

3. **User Already Exists**  
   <img src="https://github.com/user-attachments/assets/c4caf76a-46c9-4d6f-a31b-a8c0e66f22b6" width="400">  

4. **Invalid Soil Type**  
   <img src="https://github.com/user-attachments/assets/98836330-5499-480e-908e-333267626a49" width="400">  

5. **Empty Optional Fields**  
   <img src="https://github.com/user-attachments/assets/a29800c6-37d1-405e-a4e4-15c7988a207f" width="400">  

6. **Invalid Email**  
   <img src="https://github.com/user-attachments/assets/d15d801a-ca4d-473d-9d40-4d856b265bd1" width="400">  


#### Buyer Registration  
1. **Success**  
   <img src="https://github.com/user-attachments/assets/2faa3aae-bc36-4f91-ae92-422520421e30" width="400">  

2. **Empty Email**  
   <img src="https://github.com/user-attachments/assets/5895fd1d-a08c-44c4-ac95-d28a241dca94" width="400">  

3. **Invalid Email Format**  
   <img src="https://github.com/user-attachments/assets/cc0912fe-60cc-43b4-9844-d5b88d0a770d" width="400">  

4. **Missing Username**  
   <img src="https://github.com/user-attachments/assets/a5d1a6e7-a40b-4795-9673-94428f3281e4" width="400">  

5. **All Fields Missing**  
   <img src="https://github.com/user-attachments/assets/b8b535c6-4ec8-4a5f-92de-e2d6d854fe70" width="400">  

#### Login  
1. **Success**  
   <img src="https://github.com/user-attachments/assets/ba11d8ed-e5c3-474e-bd01-560dad16d542" width="400">  

2. **Incorrect Password**  
   <img src="https://github.com/user-attachments/assets/8b7b9d49-31a6-4e82-8103-f3d7ac993c5a" width="400">  

3. **Non-existing User**  
   <img src="https://github.com/user-attachments/assets/4173f3a6-c229-485a-907e-d6064da27f03" width="400">  

4. **Empty Email**  
   <img src="https://github.com/user-attachments/assets/f80ff7de-41a3-4fae-bea8-875520e6a8bc" width="400">  

5. **Empty Password**  
   <img src="https://github.com/user-attachments/assets/62867e9b-23f8-4af0-af68-5fa8a9f12b36" width="400">  




### Farmer Interface
### Buyer Interface
### Admin Interface
 
  


