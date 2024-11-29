import requests


# Testing scenarios for development environment only. For production, we need to use a test database.


def test_health():
    url = "http://localhost:8000/health"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "the application is running"


def test_full_scenario_personal_loan():
    url = "http://localhost:8000/loans/personal"
    payload = {
        "amount": 500000,
        "interest_rate": 5.5,
        "term_months": 360,
        "purpose": "car",
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["amount"] == 500000
    # check get request with this id
    loan_id = data["id"]
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == loan_id
    # check update request with this id
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    payload = {
        "amount": 600000,
        "interest_rate": 5.5,
        "term_months": 360,
        "purpose": "car",
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 600000
    # check delete request with this id
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Loan deleted"
    # check get request with this id
    url = f"http://localhost:8000/loans/personal/{loan_id}"
    response = requests.get(url)
    assert response.status_code == 404


def test_full_scenario_mortgage_loan():
    url = "http://localhost:8000/loans/mortgage"
    payload = {
        "amount": 500000,
        "interest_rate": 5.5,
        "term_months": 360,
        "address": "123 Main St",
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["amount"] == 500000
    # check get request with this id
    loan_id = data["id"]
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == loan_id
    # check update request with this id
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    payload = {
        "amount": 600000,
        "interest_rate": 5.5,
        "term_months": 360,
        "address": "123 Main St",
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 600000
    # check delete request with this id
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Loan deleted"
    # check get request with this id
    url = f"http://localhost:8000/loans/mortgage/{loan_id}"
    response = requests.get(url)
    assert response.status_code == 404
