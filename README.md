# Task Management API

A task management application built with Python and FastAPI. The project provides user authentication and a REST API for creating and managing personal tasks.

The application also includes a frontend that communicates with the FastAPI backend.

## Features

- User registration
- User login
- JWT-based authentication
- Protected API endpoints
- Create tasks
- View all tasks belonging to the authenticated user
- View a specific task
- Update tasks
- Delete tasks
- Mark tasks as completed
- Task ownership and authorization checks
- Request and response validation
- SQLAlchemy database integration
- CORS configuration
- Environment-based configuration
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- HTML
- CSS
- JavaScript
- Alembic

## Project Structure

```text
task-management-app/
│
├── src/
│   │
│   ├── tasks/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── users/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── constant.py
│       ├── db.py
│       ├── helpers.py
│       ├── mail.py
│       └── settings.py
│
├── .gitignore
├── .python-version
├── alembic.ini
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
Project Architecture

The backend is separated into routers, controllers, DTOs, models, and utility modules.

Client
   │
   ▼
FastAPI Router
   │
   ▼
Controller
   │
   ▼
SQLAlchemy Model
   │
   ▼
Database
Routers

The router files define the API endpoints and handle incoming HTTP requests.

src/users/router.py
src/tasks/router.py
Controllers

Controllers contain the application logic and database operations used by the routes.

src/users/controller.py
src/tasks/controller.py
DTOs

DTOs define the structure of incoming requests and outgoing responses and are used for validation.

src/users/dtos.py
src/tasks/dtos.py
Models

Models represent the database tables and their relationships.

src/users/models.py
src/tasks/models.py
Utilities

The utils package contains shared functionality used throughout the application.

src/utils/
├── constant.py
├── db.py
├── helpers.py
├── mail.py
└── settings.py
Authentication

The application uses JWT-based authentication.

A user can register an account and then log in to receive an authentication token.

The token is sent with protected requests using the Authorization header:

Authorization: Bearer <access_token>

FastAPI dependencies are used to authenticate requests before protected endpoints are executed.

Authorization

Authentication and authorization are handled separately.

Authentication verifies that the user is logged in.

Authorization verifies that the authenticated user is allowed to access or modify the requested resource.

Task-specific operations perform ownership checks so that users can only manage tasks that belong to their account.

For example, a user should not be able to update or delete another user's task simply by knowing its task ID.

API Endpoints
User Endpoints
Method	Endpoint	Authentication	Description
POST	/user/register	No	Register a new user
POST	/user/login	No	Login and receive an access token
GET	/user/is_auth	Yes	Check the current authentication status
Task Endpoints
Method	Endpoint	Authentication	Description
POST	/tasks/create	Yes	Create a new task
GET	/tasks/all_tasks	Yes	Get tasks belonging to the current user
GET	/tasks/one_task/{task_id}	Yes	Get a specific task
PUT	/tasks/update_task/{task_id}	Yes	Update a task
DELETE	/tasks/delete_task/{task_id}	Yes	Delete a task

Protected endpoints require a valid JWT token.

API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, Swagger UI can be accessed at:

http://127.0.0.1:8000/docs

The OpenAPI schema is available at:

http://127.0.0.1:8000/openapi.json

The Swagger UI can be used to test the API endpoints directly from the browser.

Running the Project
1. Clone the repository
git clone <your-repository-url>
cd task-management-app
2. Create a virtual environment

Using Python:

python -m venv .venv

On Windows PowerShell:

.venv\Scripts\activate
3. Install dependencies

This project uses uv for dependency management.

Install the project dependencies with:

uv sync

If you are using the environment created with Python instead, install the dependencies according to the project's pyproject.toml.

4. Configure environment variables

Create a .env file in the project root.

Example:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

Add any other variables required by the application's settings.

Do not use real credentials in the example above and do not commit your actual .env file to GitHub.

5. Start the development server

Run:

fastapi dev

The development server will start at:

http://127.0.0.1:8000

The API documentation will be available at:

http://127.0.0.1:8000/docs
Database

The project uses SQLAlchemy for database interaction.

Database configuration and the SQLAlchemy engine are handled in:

src/utils/db.py

The project also contains an Alembic configuration:

alembic.ini

which can be used for managing database migrations.

CORS

CORS middleware is configured in main.py so that the frontend can communicate with the FastAPI backend during development.

The current development configuration allows cross-origin requests.

For production deployment, the allowed origins should be restricted to the actual frontend domain instead of allowing every origin.

Frontend

The project includes a frontend interface for interacting with the backend API.

The frontend communicates with the FastAPI server and uses the authentication token when accessing protected endpoints.

It provides a graphical interface for working with the task management functionality instead of requiring users to interact with the API directly through Swagger or another API client.

Error Handling

The API uses HTTP status codes and FastAPI's HTTPException to handle errors.

Examples include:

Invalid credentials
Invalid request data
Missing authentication
Invalid task IDs
Tasks that do not exist
Unauthorized access to another user's task

This allows API clients and the frontend to determine whether a request was successful or failed.

Security

The project uses several basic security practices:

JWT authentication for protected endpoints
Authentication dependencies
User-specific task access
Task ownership checks
Environment variables for sensitive configuration
.gitignore for local configuration files

Sensitive information such as database credentials, JWT secret keys, email credentials, and other private configuration values should never be committed to the repository.

Environment Variables

Sensitive configuration is stored using environment variables rather than being written directly into the source code.

A local .env file can contain values such as:

DATABASE_URL=
SECRET_KEY=

The actual values should only exist in the local environment.

If you want to show other developers which variables are required, create a .env.example file containing placeholder values:

DATABASE_URL=
SECRET_KEY=

The real .env file should remain ignored by Git.

Development

The project is configured for local development using FastAPI's development server.

Running:

fastapi dev

starts the application with automatic reload enabled, allowing changes to the source code to be detected during development.

What I Learned

This project gave me practical experience building a backend application with FastAPI and working with the different parts of a REST API.

Some of the main concepts I worked with include:

Building REST APIs
FastAPI routing
Dependency injection
JWT authentication
User authentication and authorization
SQLAlchemy ORM
Database models and relationships
Pydantic validation
HTTP status codes
Error handling
CORS
Environment variables
Database migrations
API documentation
Connecting a frontend to a backend API
Structuring a Python backend into separate modules
Future Improvements

Some improvements that could be added in future versions include:

Automated tests with Pytest
More comprehensive validation
Pagination for task lists
Task priorities
Task categories
Due dates
Search and filtering
Refresh tokens
Rate limiting
More restrictive CORS configuration for production
Production deployment
CI/CD pipeline
Improved application logging
Monitoring
Project Status

The project is currently under development and was built as a practical backend development project using FastAPI.

Author

Abdul Rehman Khan

BS Computer Science
Bahria University Islamabad

GitHub:https://github.com/AbdulRehmanKhan101 

LinkedIn:https://www.linkedin.com/in/abdul-rehman-khan-758036352/