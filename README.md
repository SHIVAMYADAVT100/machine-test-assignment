# FastAPI Machine Test Project

A RESTful API built with FastAPI for managing categories and products with PostgreSQL database.

## Features

- FastAPI REST endpoints
- SQLAlchemy ORM for database operations
- PostgreSQL database support
- Pydantic for data validation
- Category and Product management endpoints
- Pagination support

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

## Prerequisites

- Python 3.8+
- PostgreSQL database

## Database Configuration

The database connection is configured in `app/core/config.py`:

```python
DATABASE_URL = "postgresql://postgres:63927@Shivam@localhost:5432/fastapi_db"
```

Modify this URL to match your PostgreSQL configuration:
- Username: `postgres`
- Password: `63927@Shivam`
- Host: `localhost`
- Port: `5432`
- Database: `fastapi_db`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SHIVAMYADAVT100/machine-test-assignment.git
```

2. Navigate to the project directory:
```bash
cd fastapi_machine_test
```

3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Ensure PostgreSQL is running and the database `fastapi_db` exists.

2. Start the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit the interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Project Structure

```
fastapi_machine_test/
├── app/
│   ├── core/              # Core configurations
│   │   └── config.py      # Database configuration
│   ├── db/                # Database session management
│   │   └── database.py   # SQLAlchemy setup
│   ├── models/            # SQLAlchemy ORM models
│   │   ├── category.py   # Category model
│   │   └── product.py   # Product model
│   ├── routes/            # API route handlers
│   │   ├── category.py   # Category routes
│   │   └── product.py   # Product routes
│   ├── schemas/           # Pydantic schemas
│   └── main.py           # Application entry point
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── .gitignore          # Git ignore file
```

## Available Endpoints

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories` | List all categories (paginated) |
| POST | `/api/categories` | Create a new category |
| GET | `/api/categories/{id}` | Get category by ID |
| PUT | `/api/categories/{id}` | Update category |
| DELETE | `/api/categories/{id}` | Delete category |

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | List all products (paginated) |
| POST | `/api/products` | Create a new product |
| GET | `/api/products/{id}` | Get product by ID |
| PUT | `/api/products/{id}` | Update product |
| DELETE | `/api/products/{id}` | Delete product |

### Other Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home endpoint |

## Pagination

List endpoints support pagination via query parameter:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 5)

Example:
```
GET /api/products?page=1
```

## Database Design

### Tables

**1. categories**
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| name | String | Not Null |

**2. products**
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| name | String | Not Null |
| description | String | Optional |
| category_id | Integer | Foreign Key → categories.id |

### Relationships

- **One Category → Many Products** (One-to-Many)
- Cascade delete: When a category is deleted, all its products are deleted

## License

MIT
