# HBnB Project - Part 2

## Overview
HBnB (Holberton B&B) is a web application that implements core functionalities similar to Airbnb. This project focuses on building the Business Logic and API layers using Python, Flask, and Flask-RESTX.

## Architecture

The application follows a layered architecture:
- **Presentation Layer**: RESTful API endpoints using Flask-RESTX
- **Business Logic Layer**: Core models and business rules
- **Service Layer**: Facade pattern for simplified access
- **Persistence Layer**: In-memory repository (to be replaced with database in Part 3)

## Features
- User management (Create, Read, Update)
- Place management (Create, Read, Update)
- Review management (Create, Read, Update, Delete)
- Amenity management (Create, Read, Update)

## Project Structure
```
hbnb/
├── app/                      # Core application code
│   ├── api/                  # API endpoints
│   │   └── v1/              # Version 1 of the API
│   ├── models/              # Business logic classes
│   ├── services/            # Facade pattern implementation
│   └── persistence/         # Data storage layer
├── tests/                   # Test files
├── run.py                   # Application entry point
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## Installation

### 1. Clone the repository
`git clone <repository-url>
cd hbnb
`

### 3. Install dependencies
`pip install -r requirements.txt`

## Running the Application
`python run.py`

The application will start on `http://localhost:5000`

### API Documentation
Access the Swagger UI at: `http://localhost:5000/api/v1/`

## Testing

### Run all tests
`python -m unittest discover tests`
