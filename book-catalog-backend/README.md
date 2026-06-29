# 📚 Book Catalog API

A RESTful Book Catalog API built with **Flask**, **SQLite**, **SQLAlchemy**, and **JWT Authentication**. This project allows authenticated administrators to manage a library's book catalog while authenticated users can browse and search books.

Developed as part of the **QSkill Backend Development Internship**.

---

## Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Role-based Authorization (Admin / Member)

### Book Management

* Create a Book *(Admin only)*
* Update a Book *(Admin only)*
* Delete a Book *(Admin only)*
* Clear Entire Catalog *(Admin only)*
* View All Books Paginated
* View Book by ID
* Search Books by Title or Author
* Book Statistics

---

## Tech Stack

* Flask
* Flask SQLAlchemy
* Flask JWT Extended
* Flask Migrate
* SQLite
* Alembic

---

## Project Structure

```
book-catalog-backend/

├── app/
│   ├── decorators.py
│   ├── extension.py
│   ├── models/
│   │   ├── book.py
│   │   └── user.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── book_routes.py
│   └── services/
│       ├── auth_service.py
│       └── book_service.py
│
├── migrations/
├── instance/
├── __init__.py
├── requirements.txt
├── run.py
└── README.md
```

---

## Installation

### Clone Repository

```bash
<<<<<<< HEAD
git clone https://github.com/T-Zec/QSkill-Backend-Internship/tree/main/book-catalog-backend>
=======
git clone https://github.com/T-Zec/QSkill-Backend-Internship/tree/main/book-catalog-backend
>>>>>>> feature/book/polish
cd book-catalog-backend
```

### Create Virtual Environment

Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URI=sqlite:///books.db
```

---

## Database Setup

Initialize migrations:

```bash
flask db init
```

Create migration:

```bash
flask db migrate -m "Initial migration"
```

Apply migration:

```bash
flask db upgrade
```

---

## Run the Application

```bash
flask run
```

or

```bash
python run.py
```

---

# API Endpoints

## Authentication

| Method | Endpoint             | Access |
| ------ | -------------------- | ------ |
| POST   | `/api/auth/register` | Public |
| POST   | `/api/auth/login`    | Public |

---

## Books

| Method    | Endpoint            | Access        |
| --------- | ------------------- | ------------- |
| GET       | `/api/books`        | Authenticated |
| GET       | `/api/books/<id>`   | Authenticated |
| GET       | `/api/books/search` | Authenticated |
| GET       | `/api/books/stats`  | Authenticated |
| POST      | `/api/books`        | Admin         |
| PUT/PATCH | `/api/books/<id>`   | Admin         |
| DELETE    | `/api/books/<id>`   | Admin         |
| DELETE    | `/api/books/clear`  | Admin         |

---

## Book Model

```json
{
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self Help",
    "publication_year": 2018,
    "availability": true,
    "created_at": "...",
    "updated_at": "...",
    "user_id": 1
}
```

---

## Authorization

The API uses JWT Authentication.

Two user roles are supported:

### Member

* View all books paginated
* View book details
* Search books
* View statistics

### Admin

* Full CRUD access
* Clear catalog
* Manage all books

---

## Registration and Login

### Registration

```json
POST /api/auth/register
{
    "username": "john_doe",
    "email": "john.doe@example.com",
    "password": "securepassword",
    "role": "admin" # default: "member"
}
```

### Login

```json
POST /api/auth/login
{
    "email": "john.doe@example.com",
    "password": "securepassword"
}
```

---

## Pagination

Books can be retrieved with pagination support:

* `page`: The page number (default: 1)
* `per_page`: Number of books per page (default: 10)

---

## Search

Books can be searched by title, author, genre, publication year and availability using query parameters:

* `title`: Search by title
* `author`: Search by author
* `genre`: Search by genre
* `publication_year`: Search by publication year
* `availability`: Search by availability

---

## Testing

The API was tested using:

* Thunder Client
* JWT Bearer Authentication
* SQLite Database

---

## Future Improvements

* Book Categories
* Borrow/Return System
* Refresh Tokens
* Docker Support
* Automated Tests

---

## License

This project was developed for educational purposes as part of the **QSkill Backend Development Internship**.
