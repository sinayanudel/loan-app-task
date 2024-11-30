# Loan Management API

This project is a FastAPI-based application for managing personal and mortgage loans. It provides endpoints to create, read, update, and delete loan records.

## Database

The application uses SQLAlchemy to interact with the database. In the development environment, SQLite is used, while in the staging and production environments, PostgreSQL is used.

### Tables

- **personal_loans:** Stores records of personal loans, including the loan amount, interest rate, term in months, and the purpose of the loan.
- **mortgage_loans:** Stores records of mortgage loans, including the loan amount, interest rate, term in months, and the address of the property.

## Security Aspects

The application uses Basic Authentication to secure its endpoints. Users must provide a valid username and password to access the API. The credentials are verified against a predefined list of users stored in the application configuration.

In the production environment, the app uses HTTPS instead of HTTP to ensure the security and privacy of the data transmitted between the client and the server. HTTPS encrypts the data, making it difficult for unauthorized parties to intercept and read the information.

**Important:** Do not push sensitive data such as passwords, API keys, or any other confidential information to the shared repository on GitHub. Use environment variables or secret management tools to handle such data securely.

## Development Environment

Create a `.env` file in the root directory of the project and add your environment-specific variables. For example:
```
BASIC_AUTH_USERNAME=your_username 
BASIC_AUTH_PASSWORD=your_password
```
Choose your preferred way to run the app locally:

1. Set up app using venv

    Run the following commands in PowerShell:
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

    Make sure Docker Desktop is running and run the following commands in PowerShell:
    ```
    # build the Docker image
    docker build -t loan-management-api .

    # run the Docker container
    docker run -d -p 8000:8000 --env-file .env --name loan-management-api-container loan-management-api

    # view the logs:
    docker logs -f loan-management-api-container
    ```
When the application is running, you can access the API documentation at http://127.0.0.1:8000/docs.

### Testing

While the application is running, run the following command in PowerShell: 
```
pytest .\tests\tests.py
```
The tests validate the full CRUD scenario including its database operations. Since we test the real app database, this method is safe only for the development environment, not for production.

## Staging Environment

The staging environment is set up using AWS services to closely mimic the production environment. The architecture includes the following components:

- **VPC (Virtual Private Cloud):** A dedicated network for the application, providing isolation and security.
- **ECS (Elastic Container Service):** Used to run the Docker containers for the application. ECS manages the deployment, scaling, and operation of the containers.
- **ECR (Elastic Container Registry):** A fully managed Docker container registry that stores the Docker images.
- **RDS (Relational Database Service):** A managed PostgreSQL database instance to store the application data.
- **IAM (Identity and Access Management):** Manages access to AWS resources, ensuring that only authorized users and services can interact with the environment.
- **AWS Secrets Manager:** Securely stores and manages sensitive information such as database credentials and API keys.

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