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

- **Presentation Layer:** Handles HTTP requests and responses, user interface, and client interactions.
- **Business Logic Layer:** Contains core domain entities and business rules.
- **Persistence Layer:** Manages data storage and retrieval, interacting with the database.

This will help ensuring maintainability, and scalability.

### Package Diagram
<img src="./Package Diagram.svg">

### Presentation Layer
**Components**: User UI, Review UI, Place UI, Amenity UI.
**Purpose**: Handles user interactions (e.g., booking a place, submitting reviews).

### class Diagram
<img src="./class diagram.svg">

## 3. Some APIs sequences diagrams
### Places List
<img src="./places list.svg">

### Review Submission
<img src="./review submission.svg">

### User Registration
<img src="./user_register.svg">

### Create new place
<img src="./Place Creation sequence diagram.svg">




