import pytest
from app import app, add

# ---- Unit Tests for add() ----
def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,5") == 6

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2;3") == 6

def test_negative_number_raises_error():
    with pytest.raises(ValueError) as e:
        add("1,-2,3")
    assert "negative numbers not allowed -2" in str(e.value)

def test_multiple_negatives():
    with pytest.raises(ValueError) as e:
        add("1,-2,3,-4")
    assert "negative numbers not allowed -2,-4" in str(e.value)


# ---- Integration Tests for Flask API ----
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_api_empty_string(client):
    response = client.post("/add", json={"numbers": ""})
    assert response.status_code == 200
    assert response.get_json() == {"result": 0}

def test_api_two_numbers(client):
    response = client.post("/add", json={"numbers": "1,5"})
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}

def test_api_newline(client):
    response = client.post("/add", json={"numbers": "1\n2,3"})
    assert response.status_code == 200
    assert response.get_json() == {"result": 6}

def test_api_custom_delimiter(client):
    response = client.post("/add", json={"numbers": "//;\n1;2"})
    assert response.status_code == 200
    assert response.get_json() == {"result": 3}

def test_api_negative_numbers(client):
    response = client.post("/add", json={"numbers": "1,-2,3"})
    assert response.status_code == 400
    assert "negative numbers not allowed" in response.get_json()["error"]
