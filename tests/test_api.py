import requests
from dotenv import load_dotenv
import os

# Testing scenarios for development environment only. For production, we need to use a test database.

load_dotenv()

USERNAME = os.getenv("BASIC_AUTH_USERNAME")
PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")


def get_auth():
    return requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)


def test_health():
    # Test the health endpoint to ensure the application is running
    url = "http://localhost:8000/health"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "the application is running"


def test_full_scenario_personal_loan():
    # Test creating a personal loan
    url = "http://localhost:8000/loans/personal"
    payload = {
        "amount": 500000,
        "interest_rate": 5.5,
        "term_months": 360,
        "purpose": "car",
    }
    response = requests.post(url, json=payload, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["amount"] == 500000

    # Test retrieving the created personal loan
    loan_id = data["id"]
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.get(url, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == loan_id

    # Test updating the personal loan
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    payload = {
        "amount": 600000,
        "interest_rate": 5.5,
        "term_months": 360,
        "purpose": "car",
    }
    response = requests.put(url, json=payload, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 600000

    # Test deleting the personal loan
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.delete(url, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Loan deleted"

    # Test retrieving the deleted personal loan (should return 404)
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.get(url, auth=get_auth())
    assert response.status_code == 404


def test_full_scenario_mortgage_loan():
    # Test creating a mortgage loan
    url = "http://localhost:8000/loans/mortgage"
    payload = {
        "amount": 500000,
        "interest_rate": 5.5,
        "term_months": 360,
        "address": "123 Main St",
    }
    response = requests.post(url, json=payload, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["amount"] == 500000

    # Test retrieving the created mortgage loan
    loan_id = data["id"]
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.get(url, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == loan_id

    # Test updating the mortgage loan
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    payload = {
        "amount": 600000,
        "interest_rate": 5.5,
        "term_months": 360,
        "address": "123 Main St",
    }
    response = requests.put(url, json=payload, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 600000

    # Test deleting the mortgage loan
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.delete(url, auth=get_auth())
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Loan deleted"

    # Test retrieving the deleted mortgage loan (should return 404)
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.get(url, auth=get_auth())
    assert response.status_code == 404
