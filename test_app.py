from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test for get_version endpoint
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test for check_prime endpoint
def test_check_prime_negative():
    response = client.get("/check_prime/-1")
    assert response.status_code == 200
    assert response.json() == {"number": -1, "is_prime": False}

def test_check_prime_zero():
    response = client.get("/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_one():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

def test_check_prime_two():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_three():
    response = client.get("/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_four():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_large_prime():
    response = client.get("/check_prime/97")
    assert response.status_code == 200
    assert response.json() == {"number": 97, "is_prime": True}

def test_check_prime_large_non_prime():
    response = client.get("/check_prime/100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}

def test_check_prime_boundary_case():
    response = client.get("/check_prime/999983")
    assert response.status_code == 200
    assert response.json() == {"number": 999983, "is_prime": True}
