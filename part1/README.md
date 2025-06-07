# HBnB Evolution Application - Technical Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [High-Level Architecture](#high-level-architecture)
3. [API Interaction Flow](#api-interaction-flow)
4. [Conclusion](#conclusion)

---

## 1. Introduction

### Project Overview
This document describes the architecture and design of a simplified version of an AirBnB-like application, named HBnB Evolution. The application will allow users to perform the following primary operations:
    **User Management**: Users can register, update their profiles, and be identified as either regular users or administrators.
    **Place Management**: Users can list properties (places) they own, specifying details such as name, description, price, and location (latitude and longitude). Each place can also have a list of amenities.
    **Review Management**: Users can leave reviews for places they have visited, including a rating and a comment.
    **Amenity Management**: The application will manage amenities that can be associated with places.


## 2. High-Level Architecture

### Overview
The application architecture and design follows the three-layer architecture using Facade pattern. 
This will help ensuring maintainability, and scalability.

### Package Diagram
<img src="./Package Diagram.svg">

#### Presentation Layer
- **Components**: User UI, Review UI, Place UI, Amenity UI.
- **Purpose**: Handles user interactions (e.g., booking a place, submitting reviews).

#### Business Logic Layer
- **Facades**: UserFacade, ReviewFacade, PlaceFacade, AmenityFacade.
   - **Role**: Acts as an interface for the Presentation Layer, abstracting complex operations (e.g., PlaceFacade might bundle place search + booking logic).

- **Services**: UserService, ReviewService, PlaceService, AmenityService.
   - **Role**: Contains core business rules (e.g., validating reviews, calculating pricing).

#### Persistence Layer
- **Repositories**: UserRepository, ReviewRepository, PlaceRepository, AmenityRepository.
   - **Role**: Handles database operations (CRUD) and abstracts the data store (e.g., MySQL).

### Class Diagram
<img src="./class diagram.svg">
Here’s a concise analysis of the **HBnB Class Diagram** (SVG file) with key observations, strengths, and potential improvements:

---

#### **1. Core Classes & Inheritance**
- **`BaseModel`**:  
  - Parent class with common fields (`id`, `created_at`, `updated_at`, etc.).  
  - **Child classes**: `User`, `Place`, `Review`, `Amenity` inherit from it.  
  - **Note**: Ensures consistent audit trails (timestamps, ownership) across entities.

---

#### **2. Key Classes & Attributes**
##### **`User`**
- **Fields**: `first_name`, `last_name`, `email`, `password`, `is_admin`.  
- **Methods**: `register()`, `update()`, `delete()`.  
- **Role**: Manages authentication and user profiles.  
- **Observation**: Missing `role` field (e.g., `host`/`guest` differentiation).  

##### **`Place`**  
- **Fields**: `title`, `description`, `price`, `latitude/longitude`, `owner` (User), `amenities` (list).  
- **Methods**: CRUD operations + `list_places()`.  
- **Association**: Aggregates `Amenity` (many-to-many implied).  

##### **`Review`**  
- **Fields**: `place`, `user`, `rating`, `comment`.  
- **Methods**: CRUD + `list_reviews()`.  
- **Association**: Depends on `User` and `Place` (composition).  

##### **`Amenity`**  
- **Fields**: `name`, `description`.  
- **Methods**: CRUD + `list_amenities()`.  
- **Association**: Linked to `Place` (many-to-many via `amenities` field).  

---

#### **3. Relationships**
1. **User → Place** (`0..n`):  
   - Diamond arrow (composition): A `User` owns zero-or-many `Place` objects.  
2. **User → Review** (`0..n`):  
   - Diamond arrow: A `User` writes zero-or-many `Review` objects.  
3. **Place → Review** (`0..n`):  
   - Diamond arrow: A `Place` has zero-or-many `Review` objects.  
4. **Place ↔ Amenity** (`n..n`):  
   - Bidirectional association: A `Place` can have multiple `Amenity` objects, and vice versa.  

## 3. Some APIs sequences diagrams
### Places List
<img src="./places list.svg">

### Review Submission
<img src="./review submission.svg">

### User Registration
<img src="./user_register.svg">

### Create new place
<img src="./Place Creation sequence diagram.svg">




