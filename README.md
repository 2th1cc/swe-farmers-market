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

#### Relationship between entities:
We defined these relationships to the entities based on real-world experiences. We used 2
types of relationship definition - cardinality and participation:
##### Farmer and Farm
- A Farmer can manage multiple Farms (1 relationship between Farmer and Farm).
- Every farm must belong to a farmer (total participation of the Farm entity).
- Not every farmer has to have a farm (partial participation of the Farmer entity).
##### Farm and Product
- A Farm can list multiple Products (1 relationship between Farm and Product).
- Every product must be grown on a farm (total participation of the Product entity).
- Not every farm must have a product (partial participation of the Farm entity).
##### Buyer and Order
- A Buyer can place multiple Orders (1 relationship between Buyer and Order).
- Not every buyer places an order (partial participation of the Buyer entity).
- Every order must be placed by a buyer (total participation of the Order entity).
##### Order and Payment
- An Order can have one Payment (1:1 relationship between Order and Payment).
- Every order must be paid for (total participation of the Order entity).
- Every payment must be linked to an order (total participation of the Payment entity).
##### Order and Delivery
- An Order can have one Delivery (1:1 relationship between Order and Delivery).
- Every order must be delivered (total participation of the Order entity).
- Every delivery must be linked to an order (total participation of the Delivery entity).
##### Order and Product
- An Order can include multiple Products, and a Product can be part of multiple Orders (M:
N relationship).
- An associative entity called OrderDetails is created to capture this relationship.
##### Order and OrderDetails
- An Order can have multiple OrderDetails as this essentially just describes the details of
each product that is in order (1 relationship between Order and OrderDetails).
- OrderDetails cannot exist without Order (total participation of the Order entity).
Product and OrderDetails
- A Product can be included in multiple OrderDetails as it can be in several orders (1
relationship between Product and OrderDetails).
- Every entry in OrderDetails must reference a Product (total participation of the Product
entity).

**Defining attributes of the entities and their descriptions**:
We have defined at least 5 attributes for each entity and defined primary and foreign keys based
on what type of relationship each entity has with each other:

#### Table 1. Attributes of Each Entity

| Entity        | Attribute          | Data Type     | Description                                                                             |
|---------------|--------------------|---------------|-----------------------------------------------------------------------------------------|
| **Farmer**    | FarmerID           | INT (PK)      | Unique identifier for the farmer.                                                      |
|               | Name               | VARCHAR       | Full name of the farmer.                                                               |
|               | Email              | VARCHAR       | Email address of the farmer.                                                           |
|               | Phone              | VARCHAR       | Phone number of the farmer.                                                            |
|               | RegistrationDate   | DATE          | Date when the farmer registered in the system.                                         |
| **Buyer**     | BuyerID            | INT (PK)      | Unique identifier for the buyer.                                                       |
|               | Name               | VARCHAR       | Full name of the buyer.                                                                |
|               | Email              | VARCHAR       | Email address of the buyer.                                                            |
|               | Phone              | VARCHAR       | Phone number of the buyer.                                                             |
|               | RegistrationDate   | DATE          | Date when the buyer registered in the system.                                          |
|               | Address            | VARCHAR       | The physical address of the buyer for deliveries.                                      |
| **Product**   | ProductID          | INT (PK)      | Unique identifier for the product.                                                     |
|               | Name               | VARCHAR       | Name of the product (e.g., carrots, tomatoes).                                         |
|               | Category           | VARCHAR       | Type or category of the product (e.g., vegetables, fruits).                            |
|               | Price              | DECIMAL       | Price per unit of the product.                                                         |
|               | StockQuantity      | INT           | Available quantity of the product in stock.                                            |
|               | Unit               | VARCHAR       | Unit of measurement (e.g., kg, lbs, pieces).                                           |
|               | FarmID (FK)        | INT           | Foreign key referencing Farm entity.                                                   |
| **Farm**      | FarmID             | INT (PK)      | Unique identifier for the farm.                                                        |
|               | Name               | VARCHAR       | Name of the farm.                                                                      |
|               | Location           | VARCHAR       | Physical location of the farm.                                                         |
|               | Size               | DECIMAL       | Size of the farm (in acres or hectares).                                               |
|               | SoilType           | VARCHAR       | Type of soil on the farm (e.g., loamy, sandy).                                         |
|               | EstablishedDate    | DATE          | Date when the farm was established.                                                    |
|               | FarmerID (FK)      | INT           | Foreign key referencing Farmer entity.                                                 |
| **Order**     | OrderID            | INT (PK)      | Unique identifier for the order.                                                       |
|               | OrderDate          | DATE          | Date when the order was placed.                                                        |
|               | TotalAmount        | DECIMAL       | Total amount of the order (calculated from products).                                  |
|               | OrderStatus        | VARCHAR       | Current status of the order (e.g., pending, shipped).                                  |
|               | PaymentMethod      | VARCHAR       | Method of payment (e.g., credit card, PayPal).                                         |
|               | BuyerID (FK)       | INT           | Foreign key referencing Buyer entity.                                                  |
| **Payment**   | PaymentID          | INT (PK)      | Unique identifier for the payment.                                                     |
|               | PaymentDate        | DATE          | Date when the payment was made.                                                        |
|               | Amount             | DECIMAL       | Amount paid.                                                                           |
|               | PaymentMethod      | VARCHAR       | Method used for the payment (e.g., credit card, bank transfer).                        |
|               | PaymentStatus      | VARCHAR       | Status of the payment (e.g., completed, pending).                                      |
|               | OrderID (FK)       | INT           | Foreign key referencing Order entity.                                                  |
| **Delivery**  | DeliveryID         | INT (PK)      | Unique identifier for the delivery.                                                    |
|               | DeliveryDate       | DATE          | Date when the order was delivered.                                                     |
|               | DeliveryStatus     | VARCHAR       | Current status of the delivery (e.g., in transit, delivered).                          |
|               | CourierService     | VARCHAR       | Name of the courier service handling the delivery.                                     |
|               | DeliveryAddress    | VARCHAR       | Address where the order was delivered.                                                 |
|               | OrderID (FK)       | INT           | Foreign key referencing Order entity.                                                  |
| **OrderDetails** | OrderID (FK, PK) | INT          | Foreign key referencing Order entity. Also composes the primary key of the entity.     |
|               | ProductID (FK, PK) | INT           | Foreign key referencing Product entity. Also composes the primary key of the entity.   |
|               | Quantity           | INT           | Quantity of the product in the order.                                                  |
|               | Price              | DECIMAL       | Price of the product in the order.                                                     |

#### Drawing ERD

After identifying the entities and all the relationships needed for the system to work we began
the creation of the ERD. The team used the draw.io tool as recommended in order to fulfil that
task. ERD is really useful in visualizing all the connections between entities and how the system
should work. We paid special attention to the implementation of primary and foreign keys,
including constraints. This is the resulting diagram:


<img src="https://github.com/user-attachments/assets/d84c3cdd-6589-4c26-ad01-15254f2cae93" width="650">


The diagrams helped guide the design and implementation of the database and system by providing a clear, visual representation of the relationships, attributes, and structure.

---

### Database

#### **SQLite3 Schema**

This schema reflects a Django-based system for managing farmers, buyers, and products in a farmer market system. Each role (Farmer or Buyer) extends the base users_customuser and interacts with products, orders, and delivery methods. The use of Many-to-Many relationships for permissions and groups enhances flexibility for user management.

```sql
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS "orders_deliverymethod" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE, "description" text NULL, "type" varchar(20) NOT NULL);
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_customuser_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_customuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customuser_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_buyer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone" varchar(15) NOT NULL, "registration_date" date NOT NULL, "address" varchar(255) NOT NULL, "default_delivery_method_id" bigint NULL REFERENCES "orders_deliverymethod" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL UNIQUE REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "preferred_payment_method" varchar(50) NULL);
CREATE TABLE IF NOT EXISTS "users_farmer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "phone" varchar(15) NOT NULL, "registration_date" date NOT NULL, "is_approved" bool NOT NULL, "rejection_feedback" text NULL, "farm_name" varchar(255) NULL, "farm_location" varchar(255) NULL, "farm_size" varchar(100) NULL, "soil_type" integer unsigned NOT NULL CHECK ("soil_type" >= 0), "user_id" bigint NOT NULL UNIQUE REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "farm_description" text NULL);
CREATE UNIQUE INDEX "users_customuser_groups_customuser_id_group_id_76b619e3_uniq" ON "users_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "users_customuser_groups_customuser_id_958147bf" ON "users_customuser_groups" ("customuser_id");
CREATE INDEX "users_customuser_groups_group_id_01390b14" ON "users_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "users_customuser_user_permissions_customuser_id_permission_id_7a7debf6_uniq" ON "users_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "users_customuser_user_permissions_customuser_id_5771478b" ON "users_customuser_user_permissions" ("customuser_id");
CREATE INDEX "users_customuser_user_permissions_permission_id_baaa2f74" ON "users_customuser_user_permissions" ("permission_id");
CREATE INDEX "users_buyer_default_delivery_method_id_623a5395" ON "users_buyer" ("default_delivery_method_id");
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE IF NOT EXISTS "authtoken_token" ("key" varchar(40) NOT NULL PRIMARY KEY, "created" datetime NOT NULL, "user_id" bigint NOT NULL UNIQUE REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "farmer_app_test" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "one" varchar(255) NOT NULL);
CREATE TABLE IF NOT EXISTS "products_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "category" varchar(10) NOT NULL, "description" text NOT NULL, "price" decimal NOT NULL, "quantity" integer NOT NULL, "is_out_of_stock" bool NOT NULL, "user_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "products_lowstocknotification" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "is_read" bool NOT NULL, "farmer_id" bigint NOT NULL REFERENCES "users_customuser" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "products_productimage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL, "product_id" bigint NOT NULL REFERENCES "products_product" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "products_product_user_id_e04f062e" ON "products_product" ("user_id");
CREATE INDEX "products_lowstocknotification_farmer_id_aac91bc6" ON "products_lowstocknotification" ("farmer_id");
CREATE INDEX "products_lowstocknotification_product_id_850eec11" ON "products_lowstocknotification" ("product_id");
CREATE INDEX "products_productimage_product_id_e747596a" ON "products_productimage" ("product_id");
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE TABLE IF NOT EXISTS "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "domain" varchar(100) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_crop" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "user_type" smallint unsigned NOT NULL CHECK ("user_type" >= 0), "email" varchar(254) NOT NULL UNIQUE, "phone_number" varchar(15) NOT NULL);
CREATE TABLE IF NOT EXISTS "users_farmer_crops_grown" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "farmer_id" bigint NOT NULL REFERENCES "users_farmer" ("id") DEFERRABLE INITIALLY DEFERRED, "crop_id" bigint NOT NULL REFERENCES "users_crop" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "users_farmer_crops_grown_farmer_id_crop_id_05f9d7eb_uniq" ON "users_farmer_crops_grown" ("farmer_id", "crop_id");
CREATE INDEX "users_farmer_crops_grown_farmer_id_838c99b0" ON "users_farmer_crops_grown" ("farmer_id");
CREATE INDEX "users_farmer_crops_grown_crop_id_6df7d0b9" ON "users_farmer_crops_grown" ("crop_id");
```

#### Creating samples:

To test the functionality of the system and the script written we created 50 rows of sample data
as recommended across all tables. This number of data was necessary as a large dataset helps
better with testing the functionality of the database and provides an understanding of how the
system will work with real-world problems. We then inserted the created samples into SQL.
Here is the dataset:
```sql
INSERT INTO users_customuser (password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, user_type, email, phone_number)
VALUES
('hashed_password1', NULL, 0, 'farmer1', 'John', 'Doe', 0, 1, CURRENT_TIMESTAMP, 1, 'farmer1@example.com', '1234567890'),
('hashed_password2', NULL, 0, 'buyer1', 'Jane', 'Smith', 0, 1, CURRENT_TIMESTAMP, 2, 'buyer1@example.com', '0987654321'),
('hashed_password3', NULL, 0, 'farmer2', 'Alice', 'Brown', 0, 1, CURRENT_TIMESTAMP, 1, 'farmer2@example.com', '1122334455'),
('hashed_password4', NULL, 0, 'buyer2', 'Bob', 'Taylor', 0, 1, CURRENT_TIMESTAMP, 2, 'buyer2@example.com', '2233445566'),
('hashed_password5', NULL, 0, 'admin1', 'Chris', 'Admin', 1, 1, CURRENT_TIMESTAMP, 0, 'admin1@example.com', '3344556677');

INSERT INTO orders_deliverymethod (name, description, type)
VALUES
('Standard', 'Standard delivery within 5-7 business days.', 'regular'),
('Express', 'Express delivery within 1-2 business days.', 'priority'),
('Pickup', 'Pickup from the farm.', 'local'),
('Drone', 'Drone delivery in selected areas.', 'premium'),
('Overnight', 'Overnight delivery service.', 'express');

INSERT INTO users_farmer (phone, registration_date, is_approved, rejection_feedback, farm_name, farm_location, farm_size, soil_type, user_id, farm_description)
VALUES
    ('1234567890', CURRENT_DATE, 1, NULL, 'Green Farm', 'North Valley', '10 acres', 3, 6, 'Sustainable organic farming.'),
    ('1122334455', CURRENT_DATE, 1, NULL, 'Sunny Fields', 'West Hill', '15 acres', 2, 7, 'Famous for premium corn.'),
    ('4455667788', CURRENT_DATE, 0, 'Pending review', NULL, NULL, NULL, 0, 8, NULL),
    ('9988776655', CURRENT_DATE, 1, NULL, 'Moonlit Farms', 'East Side', '20 acres', 4, 9, 'Focuses on rice and wheat.'),
    ('5566778899', CURRENT_DATE, 1, NULL, 'Harvest Valley', 'South Ridge', '8 acres', 1, 10, 'Specializes in seasonal crops.');

INSERT INTO users_buyer (phone, registration_date, address, default_delivery_method_id, user_id, preferred_payment_method)
VALUES
('0987654321', CURRENT_DATE, '123 Main Street, Cityville', 1, 2, 'Credit Card'),
('2233445566', CURRENT_DATE, '456 Oak Avenue, Townsville', 2, 4, 'Cash'),
('6677889900', CURRENT_DATE, '789 Pine Lane, Hamlet', 3, 5, 'PayPal'),
('3344556677', CURRENT_DATE, '321 Elm Road, Metro', 4, 3, 'Debit Card'),
('7788990011', CURRENT_DATE, '654 Cedar Court, Suburb', 5, 1, 'Bank Transfer');

INSERT INTO users_crop (name)
VALUES
('Wheat'),
('Rice'),
('Corn'),
('Tomatoes'),
('Carrots');

INSERT INTO users_farmer_crops_grown (farmer_id, crop_id)
VALUES
(1, 1), -- Farmer grows Wheat
(1, 3), -- Farmer grows Corn
(3, 2), -- Farmer grows Rice
(5, 4), -- Farmer grows Tomatoes
(5, 5); -- Farmer grows Carrots

INSERT INTO products_product (name, category, description, price, quantity, is_out_of_stock, user_id)
VALUES
    ('Tomatoes', 'Vegetable', 'Fresh organic tomatoes.', 2.50, 100, 0, 1),
    ('Corn', 'Grain', 'Sweet yellow corn.', 1.50, 50, 0, 3),
    ('Rice', 'Grain', 'Organic white rice.', 3.00, 0, 1, 2), 
    ('Wheat', 'Grain', 'Golden wheat.', 2.00, 75, 0, 5), -- Corrected this row
    ('Carrots', 'Vegetable', 'Crunchy fresh carrots.', 1.25, 10, 0, 5); -- Corrected this row

```

---

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

---

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

---

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


---

### Farmer Interface
### Buyer Interface
### Admin Interface
 
  


