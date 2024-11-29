# Loan Management API

This project is a FastAPI-based application for managing personal and mortgage loans. It provides endpoints to create, read, update, and delete loan records.

## Development Environment

Use these PowerShell commands to set up the application:
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

When the application is running, you can access the API documentation at http://127.0.0.1:8000/docs.

### Testing

Open PowerShell and use the `pytest` command in the project folder to run the full scenario tests while the application is running on `localhost:8000`. The tests validate the full CRUD scenario including its database operations. Since we test the real app database, this method is safe only for the development environment, not for production.

## Staging Environment

TODO

### Testing

TODO