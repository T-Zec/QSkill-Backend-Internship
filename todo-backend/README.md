# Todo Backend API

A RESTful Todo Backend built with **Flask** following the **App Factory Pattern** and **Service Layer Architecture**. The application provides secure user authentication using JWT and supports complete Todo management with pagination and filtering.

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected API Routes
* User Profile Endpoint
* Password Hashing using Werkzeug

### Todo Management

* Create Todo
* Get All Todos
* Get Todo by ID
* Update Todo
* Delete Todo
* Clear All Todos
* Mark Todo as Completed
* Mark Todo as Incomplete

### Additional Features

* User-specific Todos
* Pagination
* Filter Todos by Completion Status
* Input Validation
* Structured JSON Responses

---

## Technology Stack

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* SQLite
* python-dotenv
* Werkzeug

---

## Project Structure

```
todo-backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── config.py
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── instance/
├── .env
├── requirements.txt
├── run.py
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/T-Zec/QSkill-Backend-Internship/tree/main/todo-backend
cd todo-backend
```

### 2. Create Virtual Environment

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file.

```
DATABASE_URL=sqlite:///todo.db
JWT_SECRET_KEY=your-secret-key
```

### 5. Apply Database Migrations

```bash
flask db upgrade
```

### 6. Run the Application

```bash
python run.py
```

The server will start on:

```
http://127.0.0.1:5000
```

---

# Authentication

Register a user first.

```
POST /api/auth/register
```

Login to receive a JWT access token.

```
POST /api/auth/login
```

Use the returned token for all protected routes.

```
Authorization: Bearer <ACCESS_TOKEN>
```

Retrieve logged-in user details.

```
GET /api/auth/profile
```

---

# API Endpoints

## Authentication

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| POST   | `/api/auth/register` | Register a new user      |
| POST   | `/api/auth/login`    | Login user               |
| GET    | `/api/auth/profile`  | Get current user profile |

---

## Todo

| Method | Endpoint                     | Description           |
| ------ | ---------------------------- | --------------------- |
| POST   | `/api/todos`                 | Create Todo           |
| GET    | `/api/todos`                 | Get All Todos         |
| GET    | `/api/todos/<id>`            | Get Todo by ID        |
| PUT    | `/api/todos/<id>`            | Update Todo           |
| PATCH  | `/api/todos/<id>`            | Partial Update Todo   |
| DELETE | `/api/todos/<id>`            | Delete Todo           |
| DELETE | `/api/todos/clear`           | Delete All User Todos |
| PATCH  | `/api/todos/<id>/complete`   | Mark Todo Completed   |
| PATCH  | `/api/todos/<id>/incomplete` | Mark Todo Incomplete  |

---

# Pagination

Retrieve paginated todos.

```
GET /api/todos?page=1&per_page=10
```

Example Response

```json
{
    "success": true,
    "pagination": {
        "page": 1,
        "per_page": 10,
        "total": 25,
        "pages": 3,
        "has_next": true,
        "has_prev": false
    },
    "data": []
}
```

---

# Filtering

Retrieve only completed todos.

```
GET /api/todos?completed=true
```

Retrieve only pending todos.

```
GET /api/todos?completed=false
```

Filtering can be combined with pagination.

```
GET /api/todos?page=1&per_page=10&completed=true
```

---

# Database Schema

## User

| Field         | Type     |
| ------------- | -------- |
| id            | Integer  |
| username      | String   |
| email         | String   |
| password_hash | String   |
| created_at    | DateTime |

---

## Todo

| Field        | Type        |
| ------------ | ----------- |
| id           | Integer     |
| title        | String      |
| description  | Text        |
| is_completed | Boolean     |
| created_at   | DateTime    |
| updated_at   | DateTime    |
| user_id      | Foreign Key |

Relationship

```
User
 └── Todo (One-to-Many)
```

---

# Validation

The API validates:

* Required fields
* Duplicate users
* Invalid credentials
* Missing request data
* Todo ownership
* Maximum character limits
* Authentication using JWT

---

# HTTP Status Codes

| Code | Description        |
| ---- | ------------------ |
| 200  | Success            |
| 201  | Resource Created   |
| 400  | Bad Request        |
| 401  | Unauthorized       |
| 404  | Resource Not Found |

---

# Project Highlights

* App Factory Pattern
* Service Layer Architecture
* Blueprint-based Routing
* SQLAlchemy ORM
* Database Migrations
* JWT Authentication
* Password Hashing
* Pagination
* Filtering
* User-specific Resource Access

---

# Future Improvements

* Refresh Tokens
* Password Reset
* Email Verification
* Swagger / OpenAPI Documentation
* Automated Testing
* Docker Deployment

---

## Author

Developed as part of the **QSkill Backend Development Internship** using Flask.
