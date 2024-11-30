# Loan Management API

This project is a FastAPI-based application for managing personal and mortgage loans. It provides endpoints to create, read, update, and delete loan records.

## Security Aspects

The application uses Basic Authentication to secure its endpoints. Users must provide a valid username and password to access the API. The credentials are verified against a predefined list of users stored in the application configuration.

In the production environment, the app use HTTPS instead of HTTP to ensure the security and privacy of the data transmitted between the client and the server. HTTPS encrypts the data, making it difficult for unauthorized parties to intercept and read the information.

**Important:** Do not push sensitive data such as passwords, API keys, or any other confidential information to the shared repository on GitHub. Use environment variables or secret management tools to handle such data securely.

## Development Environment

Create a `.env` file in the root directory of the project and add your environment-specific variables. For example:
```
BASIC_AUTH_USERNAME=your_username 
BASIC_AUTH_PASSWORD=your_password
```
Choose your preffered way to run the app locally:

1. Set up app using venv

    Run the following commands in powershell:
    ```
    # create new env
    python -m venv env

    # activate env
    Set-ExecutionPolicy Unrestricted -Scope Process
    .\env\Scripts\Activate.ps1

    # install dependencies
    pip install -r requirements.txt

    # run app
    uvicorn app.main:app --reload
    ```
2. Set up app using Docker

    Run the following commands in powershell:
    ```
    # build the Docker image
    docker build -t loan-management-api .

    # run the Docker container
    docker run -d -p 8000:8000 --env-file .env --name loan-management-api-container loan-management-api
    ```
When the application is running, you can access the API documentation at http://127.0.0.1:8000/docs.

### Testing

While the application is running, run the following command in powershell: 
```
pytest .\tests\tests.py
```
The tests validate the full CRUD scenario including its database operations. Since we test the real app database, this method is safe only for the development environment, not for production.

## Staging Environment

TODO

### Deployment

TODO

### Testing

TODO

### Logs

TODO

## Prod Environment

TODO

### Deployment

TODO

### Testing

TODO

### Logs

TODO