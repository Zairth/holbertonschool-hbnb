# **HBnB - Technical Documentation**

## **1. Introduction**

The **HBnB** project is a platform that allows users to manage places and accommodations, where users can create accounts, list places, submit reviews, and more. This document provides a comprehensive technical overview of the system architecture, including key diagrams and design decisions that guide the implementation process.

This technical documentation is designed to serve as a reference for developers throughout the project, outlining the high-level architecture, detailed business logic, and the API interactions that will be part of the HBnB platform.

---

## **2. High-Level Architecture**

The high-level architecture diagram provides an overview of the key layers and their interactions in the HBnB system. The architecture follows a layered approach, which includes the Presentation Layer, the Business Logic Layer, and the Persistence Layer.

### **High-Level Package Diagram**

![High-Level Package Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739701905-t0.png)

The diagram shows the following:

- **Presentation Layer**: This layer handles user interactions and contains components for managing user profiles, places, reviews, and amenities.
- **Business Logic Layer**: Contains the core logic of the system, including the models for users, places, reviews, and amenities.
- **Persistence Layer**: The database where all data is stored.

The layers interact as follows:

- The **Presentation Layer** communicates with the **Business Logic Layer** using the Facade Pattern.
- The **Business Logic Layer** handles data operations, interacting with the **Persistence Layer** to store and retrieve data.

---

## **3. Business Logic Layer**

The **Business Logic Layer** is the core of the system, where the main business rules and logic reside. This section describes the classes that make up the Business Logic Layer, including their attributes, methods, and relationships.

### **Detailed Class Diagram for Business Logic Layer**

![Detailed Class Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739702268-t1.png)

### **Class Descriptions**

#### **User**
- **Attributes**:
  - `UUID4 id`: A unique identifier for the user.
  - `String first_name`, `String last_name`, `String email`: User's personal information.
  - `String password`: Encrypted password.
  - `String country`, `String mobile_number`: Contact details.
  - `Date created_profil`, `Date updated_profil`: Date attributes for tracking profile creation and update.
- **Methods**:
  - `create()`, `update()`, `delete()`: Methods for creating, updating, and deleting user profiles.

#### **Place**
- **Attributes**:
  - `UUID4 id`: Unique identifier for each place.
  - `String name`, `String description`: Basic details of the place.
  - `jpg pictures`, `Integer price`: Media and pricing information.
  - `String location`, `String city`: Location-related details.
  - `Date created_place`, `Date updated_place`: Creation and update timestamps.
- **Methods**:
  - `create()`, `update()`, `delete()`: Methods for managing place details.

#### **Review**
- **Attributes**:
  - `UUID4 id`: Unique identifier for each review.
  - `String content`: Review content.
  - `String user_name`, `Int rating`: Reviewer's name and rating.
  - `Date created_review`, `Date updated_review`: Creation and update dates for reviews.
- **Methods**:
  - `create()`, `update()`, `delete()`: Methods for managing reviews.

#### **Amenity**
- **Attributes**:
  - `UUID4 id`: Unique identifier for amenities.
  - `String name`: The name of the amenity.
  - `Date created_amnety`, `Date updated_amnety`: Date attributes for tracking the creation and update of amenities.
- **Methods**:
  - `create()`, `update()`, `delete()`: Methods for managing amenities.

---

## **4. API Interaction Flow**

In this section, we describe the flow of API calls between the user, the API, the business logic, and the database. The sequence diagrams provide a detailed view of how users interact with the system.

### **Sequence Diagrams for API Calls**

#### **User Registration**

![User Registration Sequence Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739702080-t2-user-registration.png)

**Flow Explanation**:

- The user sends a registration request to the API.
- The API validates the user data and checks the database for existing users.
- Once the user is validated, the new user data is saved in the database, and the API returns a success response to the user.

---

#### **Place Creation**

![Place Creation Sequence Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739702106-t2-place-creation.png)

**Flow Explanation**:

- The user sends a place creation request to the API.
- The API validates the place data and checks the database for existing places.
- Once validated, the new place is saved in the database, and the API returns a success response.

---

#### **Review Submission**

![Review Submission Sequence Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739702131-t2-review-submission.png)

**Flow Explanation**:

- The user sends a review submission request to the API.
- The API validates the review data and checks the database for the corresponding place.
- Once the place is found, the review is saved in the database, and the API returns a success response.

---

#### **Fetching a List of Places**

![Fetching Places Sequence Diagram](https://image.noelshack.com/fichiers/2025/07/7/1739702151-t2-fetching-a-list-of-places.png)

**Flow Explanation**:

- The user sends a request to the API to fetch places based on search criteria.
- The API processes the criteria and queries the database for matching places.
- The database returns the list of places, and the API sends the list back to the user.
