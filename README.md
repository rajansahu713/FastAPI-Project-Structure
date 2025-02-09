# FastAPI-Project-Structure

This repository provides a basic project structure for developing web applications with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## Overview

This project structure is designed to provide a clean and organized layout for developing FastAPI applications. It incorporates best practices and common patterns to ensure scalability, maintainability, and ease of development.

## Features

- **FastAPI**: Leverages the FastAPI framework for building APIs.
- **SQLAlchemy**: Uses SQLAlchemy for database interactions.
- **Pytest**: Includes test cases using Pytest.
- **SQLite**: Uses SQLite as the default database for testing.
- **Dependency Injection**: Implements dependency injection for database sessions.
- **HTML Test Reports**: Generates HTML reports for test results using `pytest-html`.

## Project Structure
```plaintext
FastAPI-Project-Structure/
    ├── database/
    │       ├── __init__.py
    │       └── db.py
    ├── auth/
    │       ├── __init__.py
    │       ├── auth.py
    │       |── constants.py
    │       |── controllers.py
    │       ├── data.py
    │       ├── models.py
    │       ├── schemas.py
    │       └── service.py
    ├── apps/
    │       ├── blog/
    │       │       ├── __init__.py
    │       │       ├── controllers.py
    │       │       ├── data.py
    │       │       ├── models.py
    │       │       ├── schemas.py
    │       │       └── service.py
    │       └── __init__.py
    ├── common/
    │       ├── constants.py
    │       ├── helper_function.py
    │       └── http_exceptions.py
    ├── test/
    │       ├── blog_app_test.py
    │       └── test_data.json
    |── __init__.py
    ├── .env
    |── .gitignore
    |── pre-commit-config.yaml
    |── docker-compose.yml
    |── Dockerfile
    |── main.py
    ├── README.md
    ├── requirements.txt
    └── routes.py
```

## Lets understand the project structure
- **database**: This folder contains the database-related code, including the database session setup and the models
- **auth**: This folder contains the authentication-related code, including the controllers, models, schemas, and services
- **apps**: This folder contains all the code according to apps wise like for blogs suppose in future if we create analytics app then we will create a folder inside apps and put all the code related to analytics app
- **common**: This folder contains the common code that can be used across the application, such as constants, helper functions, and custom exceptions



### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### To Clone the repository:
```sh
git clone https://github.com/yourusername/FastAPI-Project-Structure.git
cd FastAPI-Project-Structure
```

### Installation
```
pip install -r requirements.txt
```

> To check the pre-commit hooks
```sh
pre-commit run --all-files
```
> Clone the repository:
```bash
   git clone https://github.com/yourusername/FastAPI-Project-Structure.git
   cd FastAPI-Project-Structure
```

> To run pre-commit hooks
```bash
pre-commit run --all-files
```

> Sometime you will get false positive error in pre-commit hooks so to skip the pre-commit hooks use the below command
```bash
git commit -m "Your commit message" --no-verify
```

> Generate the Yesting report with pytest in html format
```bash
pytest --html=report.html
```
### Run the application
```bash
uvicorn main:app --reload
```
