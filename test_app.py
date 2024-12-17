import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_get_version():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

@pytest.mark.parametrize("number, expected_result", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (9, False),
    (11, True),
    (16, False),
    (17, True),
    (19, True),
    (20, False)
])
def test_check_prime(number, expected_result):
    response = requests.get(f"{BASE_URL}/check_prime/{number}")
    assert response.status_code == 200
    assert response.json()["is_prime"] == expected_result
