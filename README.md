# Farmer Market System

Nazarbayev University
SOFTWARE ENGINEERING CSCI 361

**Team Members**:

- Lazzat Zhengissova
- Akmaral Ayazbay
- Yeldos Nurpeissov
- Azimzhan Abdrakhmanov
- Zeindi Adakhajiyev
- Yezhan Tugralin

## Contents

- [Technology Stack](#technology-stack)
- [Diagrams](#diagrams)
  - [Class Diagram](#class-diagram)
  - [Component Diagram](#component-diagram)
  - [Use Case Diagram](#use-case-diagram)
  - [Activity Diagram](#activity-diagram)
  - [ER Diagram](#er-diagram)
  - 
- [Software Details](#software-details)
  - [User Registration and Authentification](#user-registration-and-authentification)
  - [Farmer Interface](#farmer-interface)
  - [Buyer Interface](#buyer-interface)
  - [Admin Interface](#admin-interface)  

## Technology Stack

The Farmers Market System is a specialized platform developed to improve the interaction between farmers and buyers, providing a streamlined experience for managing agricultural products. Each technology used in the system was carefully chosen to ensure efficiency, security, and ease of use.

For the user interface, we utilized Django's templating engine combined with standard web technologies like HTML, CSS, and JavaScript. This enabled us to design a clean, responsive, and easy-to-navigate interface tailored to user needs.

For the mobile stack, the system can be expanded using Flutter, a cross-platform framework known for its performance and flexibility. Flutter would allow the development of a single mobile application for both iOS and Android, maintaining a consistent user experience across devices.

On the backend, Django was selected as the primary framework due to its robust capabilities for handling complex operations. It simplifies tasks such as database interactions, user authentication, and API creation. To expose functionalities through APIs, Django REST Framework (DRF) was employed, which offers tools to build secure and efficient endpoints.

SQLite3 serves as the database for this project. Its lightweight nature and simplicity make it an excellent choice for the scale of this system. The database manages all essential entities, such as products, orders, users, and notifications, in a structured manner.

Additional functionality was incorporated using tools like Pillow, which enables image handling and optimization. Filtering and search functionalities were enhanced through Django Filters, allowing users to locate products or information quickly.

Together, this stack—Django for backend operations, SQLite3 for data storage, and standard frontend tools—creates a system designed to meet the needs of the farming community. The result is a reliable, functional platform that connects farmers and buyers effectively.

## Diagrams

To better understand how a system works and simplify further planning we have created four UML diagrams: Class, Component, Use Case and Activity  diagrams. These diagrams are presented below.

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

### Component Diagram

<img src="https://github.com/user-attachments/assets/ab7d396c-f1f6-4c61-a75b-29daec5061c7" width="650">

This Component Diagram provides a high-level view of the Farmer's Market platform and how its various components interact:
- **Frontend API**: Acts as a bridge between the mobile and web applications and the backend services.
  - **Mobile Application**: A user-friendly app for consumers and farmers to interact with the platform, accessible on the go.
  - **Web Application**: A browser-based interface offering similar functionality as the mobile app, designed for desktop users.
- **API Gateway**: A centralized entry point that routes incoming requests from the frontend apps to the appropriate backend services. It handles security, load balancing, and rate limiting.
- **Backend Services**: Comprises multiple modular services for specific tasks:
  1. **Product Management Service**: Manages product listings, interacting with the Product Data database.
  2. **Order Management Service**: Manages the entire order lifecycle, integrates with external payment and logistics services, and stores data in the Order Data database.
  3. **Chat Service**: Facilitates direct communication between buyers and farmers, storing chat history in the Chat Data database.
  4. **Notification Service**: Sends real-time notifications to users about order updates or new messages.
  5. **Authentication Service**: Handles user authentication and authorization, working with the User Data database.
  6. **Reporting and Analytics Service**: Generates reports on user behavior, sales data, and platform performance, storing results in the Sales Data database.
  7. **Search Service**: Helps users quickly find products and services based on data.
- **Databases**: Various databases store data specific to each service:
  - **Product Data**: Stores product listings.
  - **User Data**: Stores user profiles and authentication details.
  - **Order Data**: Stores information on orders and their status.
  - **Chat Data**: Stores chat histories.
  - **Sales Data**: Stores transactional data for reporting.
- **External APIs**: Integrates with third-party services:
  1. **Payment Gateway**: Facilitates secure payment processing between buyers and farmers.
  2. **Logistics Provider API**: Manages shipping logistics and order tracking, ensuring timely deliveries.
This architecture ensures modularity, scalability, and effective interaction between various services, making the system efficient and user-friendly.


### Use Case Diagram

<img src="https://github.com/user-attachments/assets/f4199348-8ea4-47ae-beb5-ea51f5820cd8" width="650">

This use case diagram focuses on enhancing the Farmer's Market System, streamlining interactions and responsibilities between users:

- **Farmer Product Management**: Farmers can list, update, and manage their products, track inventory, and generate sales reports.
- **Buyer Interaction**: Buyers can register, log in, manage profiles, negotiate prices, and track orders.
- **Order Tracking**: Both farmers and buyers can track the status of orders, ensuring timely delivery and order fulfillment.
- **Admin Oversight**: Admins are responsible for monitoring system functionality, managing users, and overseeing platform performance.
- **Logistics and Delivery**: The logistics provider ensures smooth delivery by managing shipping and tracking product deliveries.
- **Payment Processing**: The Payment Gateway securely handles transactions between buyers and farmers, ensuring safe and timely payments.

### Activity Diagram

<img src="https://github.com/user-attachments/assets/b35c36f3-0d7f-4843-815f-a6ab305f966a" width="650">

The activity diagram illustrates the entire process flow in the Farmer's Market System, detailing the tasks performed by each entity:

- User: The user initiates the process by registering and verifying their account. Once verified, they log in, receive notifications, and interact with the platform through the dashboard. If needed, their account may be temporarily locked after multiple failed login attempts.
- Farmer: The farmer manages their profile and product listings after logging in. They update product details, inventory, and generate reports on sales and offers. The farmer’s activities revolve around product management and interacting with potential buyers.
- Buyer: The buyer searches for products, adds them to their cart, and proceeds with payment. Once payment is processed, they can track their order status and generate offers or reports related to their buying activities.
- System: The system interacts with multiple databases, validating data and confirming actions. It ensures smooth operation by sending notifications, confirming actions like orders and trades, and keeping all entities informed.
- Error Handling: The system checks for validation and error recovery throughout the process, ensuring that login and verification steps are correctly handled.

Overall, this diagram shows the complete cycle of operations, from registration to order tracking and reporting, providing a seamless experience for all actors involved in the system.

### ER Diagram
1. **Entities**
   - **Farmer**: Represents individuals who manage farms and sell products.
   - **Buyer**: Represents individuals purchasing products.
   - **Farm**: Represents a physical location where products are cultivated.
   - **Product**: Represents items sold by farmers (e.g., vegetables, fruits).
   - **Order**: Represents purchases made by buyers.
   - **Payment**: Represents the payments made for orders.
   - **Delivery**: Represents the delivery details for orders.
   - **OrderDetails**: Captures details of products included in an order.
2. **Relations**
   - **Farmer OWNS Farms**: (one-to-many) One Farmer can own multiple Farms, but each Farm belongs to one Farmer.
   - **Farm PRODUCES Products**: (one-to-many) One Farm can produce multiple Products, but each Product comes from one Farm.
   - **Buyer PLACES Orders**: (one-to-many) One Buyer can place multiple Orders, but each Order is placed by one Buyer.
   - **Order INCLUDES Products**: (many-to-many) One Order can include multiple Products, and one Product can be included in multiple Orders.
   - **Order HAS Payment**: (one-to-one) One Order has exactly one Payment, and each Payment is linked to one Order.
   - **Order HAS Delivery**: (one-to-one) One Order has exactly one Delivery, and each Delivery is linked to one Order.
   - **OrderDetails DESCRIBES Products in Orders**: (one-to-many) One Order can have multiple entries in OrderDetails, and each entry is associated with one Product.
   - **Delivery HANDLES Order**: (one-to-one) Each Delivery handles one Order, and each Order is managed by one Delivery.
   - **Product APPEARS in OrderDetails**: (one-to-many) One Product can appear in multiple OrderDetails entries, describing its involvement in different Orders.
   - **Payment SETTLES Orders**: (one-to-one) Each Payment is used to settle exactly one Order.
3. **Attributes**
   - **Farmer**: FarmerID (Primary Key), Name, Email, Phone, RegistrationDate
   - **Buyer**: BuyerID (Primary Key), Name, Email, Phone, RegistrationDate, Address
   - **Farm**: FarmID (Primary Key), Name, Location, Size, SoilType, EstablishedDate, FarmerID (Foreign Key)
   - **Product**: ProductID (Primary Key), Name, Category, Price, StockQuantity, Unit, FarmID (Foreign Key)
   - **Order**: OrderID (Primary Key), OrderDate, TotalAmount, OrderStatus, PaymentMethod, BuyerID (Foreign Key)
   - **Payment**: PaymentID (Primary Key), PaymentDate, Amount, PaymentMethod, PaymentStatus, OrderID (Foreign Key)
   - **Delivery**: DeliveryID (Primary Key), DeliveryDate, DeliveryStatus, CourierService, DeliveryAddress, OrderID (Foreign Key)
   - **OrderDetails**: OrderID (Foreign Key, Primary Key), ProductID (Foreign Key, Primary Key), Quantity, Price
4. **Cardinality**
   - Farmer to Farm: 1:M
   - Farm to Product: 1:M
   - Buyer to Order: 1:M
   - Order to Payment: 1:1
   - Order to Delivery: 1:1
   - Order to Product: M:N (handled through OrderDetails)
   - Order to OrderDetails: 1:M
   - Product to OrderDetails: 1:M
5. ERD
<img src="https://github.com/user-attachments/assets/d84c3cdd-6589-4c26-ad01-15254f2cae93" width="650">

6. Database using DBRMS

```sql
CREATE TABLE Farmer (
FarmerID INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Email VARCHAR(100) UNIQUE NOT NULL,
Phone VARCHAR(15) NOT NULL,
RegistrationDate DATE NOT NULL
);
CREATE TABLE Buyer (
BuyerID INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Email VARCHAR(100) UNIQUE NOT NULL,
Phone VARCHAR(15) NOT NULL,
RegistrationDate DATE NOT NULL,
Address VARCHAR(255) NOT NULL
);
CREATE TABLE Farm (
FarmID INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Location VARCHAR(255) NOT NULL,
Size DECIMAL(10, 2),
SoilType VARCHAR(50),
EstablishedDate DATE,
FarmerID INT NOT NULL,
FOREIGN KEY (FarmerID) REFERENCES Farmer(FarmerID)
);
CREATE TABLE Product (
ProductID INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL,
Category VARCHAR(50) NOT NULL,
Price DECIMAL(10, 2) NOT NULL,
StockQuantity INT NOT NULL,
Unit VARCHAR(20) NOT NULL,
FarmID INT NOT NULL,
FOREIGN KEY (FarmID) REFERENCES Farm(FarmID)
);
CREATE TABLE "Order" (
OrderID INT PRIMARY KEY,
OrderDate DATE NOT NULL,
TotalAmount DECIMAL(10, 2) NOT NULL,
OrderStatus VARCHAR(50) NOT NULL,
PaymentMethod VARCHAR(50),
BuyerID INT NOT NULL,
FOREIGN KEY (BuyerID) REFERENCES Buyer(BuyerID)
);
CREATE TABLE Payment (
Unset
PaymentID INT PRIMARY KEY,
PaymentDate DATE NOT NULL,
Amount DECIMAL(10, 2) NOT NULL,
PaymentMethod VARCHAR(50) NOT NULL,
PaymentStatus VARCHAR(50) NOT NULL,
OrderID INT NOT NULL,
FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID)
);
CREATE TABLE Delivery (
DeliveryID INT PRIMARY KEY,
DeliveryDate DATE NOT NULL,
DeliveryStatus VARCHAR(50) NOT NULL,
CourierService VARCHAR(100) NOT NULL,
DeliveryAddress VARCHAR(255) NOT NULL,
OrderID INT NOT NULL,
FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID)
);
CREATE TABLE OrderDetails (
OrderID INT NOT NULL,
ProductID INT NOT NULL,
Quantity INT NOT NULL,
Price DECIMAL(10, 2) NOT NULL,
PRIMARY KEY (OrderID, ProductID),
FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID),
FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
```





## Software Details

### User Registration and Authentification
### Farmer Interface
### Buyer Interface
### Admin Interface
 
  


