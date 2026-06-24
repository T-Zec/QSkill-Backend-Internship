# Todo Backend API

## Overview

A RESTful Todo Backend built with Flask following the App Factory Pattern. The application supports user authentication using JWT, user-specific todo management, pagination, filtering, and complete CRUD operations.

## Features

* User Registration
* User Login
* JWT Authentication
* User Profile Endpoint
* Create Todo
* Get All Todos
* Get Single Todo
* Update Todo
* Delete Todo
* Mark Todo as Complete
* Mark Todo as Incomplete
* Pagination Support
* Filtering by Completion Status
* User-Owned Todo Records

## Technology Stack

* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* SQLite
* Python

## Installation

1. Clone the repository
2. Create virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

5. Run migrations

flask db upgrade

6. Start server

python run.py

## Authentication

Protected routes require:

Authorization: Bearer <JWT_TOKEN>

## API Endpoints

### Authentication

POST /api/auth/register
POST /api/auth/login
GET /api/auth/profile

### Todos

POST /api/todos
GET /api/todos
GET /api/todos/<id>
PUT /api/todos/<id>
DELETE /api/todos/<id>
PATCH /api/todos/<id>/complete
PATCH /api/todos/<id>/incomplete

## Pagination

GET /api/todos?page=1&per_page=10

## Filtering

GET /api/todos?completed=true
GET /api/todos?completed=false
