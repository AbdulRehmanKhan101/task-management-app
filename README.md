# Task Management API

A task management application built with Python and FastAPI. The project provides user authentication and a REST API for creating and managing personal tasks.

The application also includes a frontend that communicates with the FastAPI backend.

**Live demo:** https://abdulrehmankhan101.github.io/task-management-app/
**Live API docs (Swagger UI):** https://task-management-app-e757e6d7.fastapicloud.dev/docs

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
- Standalone Hugging Face chatbot

## Tech Stack

- Python
- FastAPI
- PostgreSQL (hosted on [Neon](https://neon.tech))
- SQLAlchemy
- Pydantic
- JWT
- HTML
- CSS
- JavaScript
- Alembic

## Deployment

| Layer    | Service                                          |
| -------- | ------------------------------------------------- |
| Backend  | [FastAPI Cloud](https://fastapicloud.com)          |
| Database | [Neon](https://neon.tech) (managed PostgreSQL)     |
| Frontend | [GitHub Pages](https://pages.github.com) (`/docs`) |

## Project Structure

```text
task-management-app/
│
├── chatbot/                # Standalone Hugging Face chatbot route
│   ├── dtos.py
│   └── router.py
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
├── migrations/            # Alembic migrations
├── docs/                  # Frontend (served via GitHub Pages)
│   └── index.html
├── .gitignore
├── .python-version
├── alembic.ini
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Project Architecture

The backend is separated into routers, controllers, DTOs, models, and utility modules.

```
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
```

### Routers

The router files define the API endpoints and handle incoming HTTP requests.

- `src/users/router.py`
- `src/tasks/router.py`

### Controllers

Controllers contain the application logic and database operations used by the routes.

- `src/users/controller.py`
- `src/tasks/controller.py`

### DTOs

DTOs define the structure of incoming requests and outgoing responses and are used for validation.

- `src/users/dtos.py`
- `src/tasks/dtos.py`

### Models

Models represent the database tables and their relationships.

- `src/users/models.py`
- `src/tasks/models.py`

### Utilities

The utils package contains shared functionality used throughout the application.

```text
src/utils/
├── constant.py
├── db.py
├── helpers.py
├── mail.py
└── settings.py
```

## Authentication

The application uses JWT-based authentication.

A user can register an account and then log in to receive an authentication token.

The token is sent with protected requests using the Authorization header:

```
Authorization: Bearer <access_token>
```

FastAPI dependencies are used to authenticate requests before protected endpoints are executed.

## Authorization

Authentication and authorization are handled separately.

Authentication verifies that the user is logged in.

Authorization verifies that the authenticated user is allowed to access or modify the requested resource.

Task-specific operations perform ownership checks so that users can only manage tasks that belong to their account.

For example, a user should not be able to update or delete another user's task simply by knowing its task ID.

## API Endpoints

### User Endpoints

| Method | Endpoint         | Authentication | Description                          |
| ------ | ---------------- | --------------- | ------------------------------------- |
| POST   | `/user/register` | No              | Register a new user                   |
| POST   | `/user/login`    | No              | Login and receive an access token     |
| GET    | `/user/is_auth`  | Yes             | Check the current authentication status |

### Task Endpoints

| Method | Endpoint                       | Authentication | Description                          |
| ------ | -------------------------------- | --------------- | ------------------------------------- |
| POST   | `/tasks/create`                  | Yes             | Create a new task                     |
| GET    | `/tasks/all_tasks`               | Yes             | Get tasks belonging to the current user |
| GET    | `/tasks/one_task/{task_id}`      | Yes             | Get a specific task                   |
| PUT    | `/tasks/update_task/{task_id}`   | Yes             | Update a task                         |
| DELETE | `/tasks/delete_task/{task_id}`   | Yes             | Delete a task                         |

Protected endpoints require a valid JWT token.

### Chatbot Endpoint

| Method | Endpoint | Authentication | Description |
| ------ | -------- | -------------- | ----------- |
| POST | `/chat` | No | Send a conversation to the standalone Hugging Face chatbot |

The chatbot is isolated from the task, user, and database functionality. It does not
read or modify application data. The Hugging Face token is kept on the backend in the
`HUGGINGFACE_API_KEY` environment variable and is never exposed to the frontend.

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, Swagger UI can be accessed at:

```
http://127.0.0.1:8000/docs
```

The OpenAPI schema is available at:

```
http://127.0.0.1:8000/openapi.json
```

The Swagger UI can be used to test the API endpoints directly from the browser. The same documentation is available on the live deployment at https://task-management-app-e757e6d7.fastapicloud.dev/docs.

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd task-management-app
```

### 2. Install dependencies

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management, which also manages the Python virtual environment automatically.

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root (see `.env.example`).

```env
DB_CONNECTION=postgresql://user:password@host/dbname?sslmode=require
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=60
ALLOWED_ORIGINS=*
HUGGINGFACE_API_KEY=your_huggingface_token
```

`DB_CONNECTION` should be a PostgreSQL connection string — e.g. from a free [Neon](https://neon.tech) project. `SECRET_KEY` can be generated with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Do not use real credentials in the example above and do not commit your actual `.env` file to GitHub.

### 4. Run database migrations

```bash
uv run alembic upgrade head
```

### 5. Start the development server

```bash
uv run fastapi dev
```

The development server will start at:

```
http://127.0.0.1:8000
```

The API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

### 6. Run the frontend locally

Open `docs/index.html` in a browser and point `API_BASE` (near the top of the `<script>` block) at `http://127.0.0.1:8000`.

## Database

The project uses SQLAlchemy for database interaction.

Database configuration and the SQLAlchemy engine are handled in:

```
src/utils/db.py
```

The project also contains an Alembic configuration (`alembic.ini`) and a `migrations/` folder used for managing database migrations.

## CORS

CORS middleware is configured in `main.py` so that the frontend can communicate with the FastAPI backend.

`ALLOWED_ORIGINS` is read from environment configuration; it currently defaults to `*` to allow any origin. For a stricter production setup, this should be restricted to the actual frontend domain (e.g. the GitHub Pages URL).

## Frontend

The project includes a frontend interface for interacting with the backend API, served from the `docs/` folder via GitHub Pages.

The frontend communicates with the FastAPI server and uses the authentication token when accessing protected endpoints.

It provides a graphical interface for working with the task management functionality instead of requiring users to interact with the API directly through Swagger or another API client.

## Error Handling

The API uses HTTP status codes and FastAPI's `HTTPException` to handle errors.

Examples include:

- Invalid credentials
- Invalid request data
- Missing authentication
- Invalid task IDs
- Tasks that do not exist
- Unauthorized access to another user's task

This allows API clients and the frontend to determine whether a request was successful or failed.

## Security

The project uses several basic security practices:

- JWT authentication for protected endpoints
- Authentication dependencies
- User-specific task access
- Task ownership checks
- Environment variables for sensitive configuration
- Secrets stored as encrypted environment variables on FastAPI Cloud in production
- `.gitignore` for local configuration files

Sensitive information such as database credentials, JWT secret keys, email credentials, and other private configuration values should never be committed to the repository.

## Environment Variables

Sensitive configuration is stored using environment variables rather than being written directly into the source code.

A local `.env` file can contain values such as:

```env
DB_CONNECTION=
SECRET_KEY=
ALGORITHM=
EXP_TIME=
```

The actual values should only exist in the local environment (or, in production, as secrets set in the FastAPI Cloud dashboard).

If you want to show other developers which variables are required, use the included `.env.example` file, which contains placeholder values only.

The real `.env` file should remain ignored by Git.

## Deployment

The live version of this project is deployed as follows:

- **Backend** — deployed to [FastAPI Cloud](https://fastapicloud.com) with `uv run fastapi deploy`. Environment variables (`DB_CONNECTION`, `SECRET_KEY`, `ALGORITHM`, `EXP_TIME`, and `HUGGINGFACE_API_KEY`) are set in the FastAPI Cloud dashboard, never committed to the repo.
- **Database** — a managed PostgreSQL instance on [Neon](https://neon.tech).
- **Frontend** — the static `docs/index.html` is served for free via **GitHub Pages**, configured in the repo's **Settings → Pages** with the source set to the `docs/` folder. Its `API_BASE` constant points at the FastAPI Cloud backend URL.

To deploy your own copy:

```bash
# Backend
uv run fastapi deploy
uv run fastapi deploy
```

Then add these variables in the FastAPI Cloud dashboard before redeploying:

```text
DB_CONNECTION=your-neon-connection-string
SECRET_KEY=your-generated-secret
ALGORITHM=HS256
EXP_TIME=60
HUGGINGFACE_API_KEY=your-huggingface-token
```

Then update `API_BASE` in `docs/index.html` to your new backend URL, push to GitHub, and enable GitHub Pages for the `docs/` folder.

## Development

The project is configured for local development using FastAPI's development server.

Running:

```bash
uv run fastapi dev
```

starts the application with automatic reload enabled, allowing changes to the source code to be detected during development.

## What I Learned

This project gave me practical experience building a backend application with FastAPI and working with the different parts of a REST API, as well as deploying a full-stack application end-to-end.

Some of the main concepts I worked with include:

- Building REST APIs
- FastAPI routing
- Dependency injection
- JWT authentication
- User authentication and authorization
- SQLAlchemy ORM
- Database models and relationships
- Pydantic validation
- HTTP status codes
- Error handling
- CORS
- Environment variables
- Database migrations
- API documentation
- Connecting a frontend to a backend API
- Structuring a Python backend into separate modules
- Deploying a FastAPI backend, a managed Postgres database, and a static frontend to production

## Future Improvements

Some improvements that could be added in future versions include:

- Automated tests with Pytest
- More comprehensive validation
- Pagination for task lists
- Task priorities
- Task categories
- Due dates
- Search and filtering
- Refresh tokens
- Rate limiting
- More restrictive CORS configuration for production
- CI/CD pipeline
- Improved application logging
- Monitoring

## Project Status

The project is deployed and functional, with a live backend, database, and frontend. It was built as a practical backend development project using FastAPI, and continues to be extended as a learning project.

## Author

**Abdul Rehman Khan**

BS Computer Science
Bahria University Islamabad

GitHub: https://github.com/AbdulRehmanKhan101
LinkedIn: https://www.linkedin.com/in/abdul-rehman-khan-758036352/