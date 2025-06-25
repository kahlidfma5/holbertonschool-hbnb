# HBnB Project - Part 2

## Project Setup

This is the initial setup for the HBnB application with:
- Presentation layer (API endpoints)
- Business logic layer (models and services)
- Persistence layer (in-memory repository)

The directory structure is organized as follows:
- The app/ directory contains the core application code.
- The api/ subdirectory houses the API endpoints, organized by version (v1/).
- The models/ subdirectory contains the business logic classes (e.g., user.py, place.py).
- The services/ subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
- The persistence/ subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python run.py`

## Run the test
`python -m unittest discover tests`
