import requests

BASE_URL = "http://localhost:5000"

def test_get_version():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"

def test_check_prime_valid():
    response = requests.get(f"{BASE_URL}/check_prime?number=7")
    assert response.status_code == 200
    assert response.json()["is_prime"] == True

def test_check_prime_not_prime():
    response = requests.get(f"{BASE_URL}/check_prime?number=8")
    assert response.status_code == 200
    assert response.json()["is_prime"] == False

def test_check_prime_negative():
    response = requests.get(f"{BASE_URL}/check_prime?number=-5")
    assert response.status_code == 200
    assert response.json()["is_prime"] == False

def test_check_prime_zero():
    response = requests.get(f"{BASE_URL}/check_prime?number=0")
    assert response.status_code == 200
    assert response.json()["is_prime"] == False

def test_check_prime_invalid_input():
    response = requests.get(f"{BASE_URL}/check_prime?number=abc")
    assert response.status_code == 400
    assert "error" in response.json()

def test_check_prime_large_number():
    response = requests.get(f"{BASE_URL}/check_prime?number=104729")
    assert response.status_code == 200
    assert response.json()["is_prime"] == True

def test_check_prime_smallest_prime():
    response = requests.get(f"{BASE_URL}/check_prime?number=2")
    assert response.status_code == 200
    assert response.json()["is_prime"] == True

def test_check_prime_one():
    response = requests.get(f"{BASE_URL}/check_prime?number=1")
    assert response.status_code == 200
    assert response.json()["is_prime"] == False

def test_get_version_status():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
