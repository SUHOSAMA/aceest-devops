import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_programs(client):
    response = client.get("/programs")
    assert response.status_code == 200
    assert "Fat Loss" in response.get_json()

def test_calculate_calories_success(client):
    response = client.post("/calories", json={
        "weight": 70,
        "program": "Fat Loss"
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["calories"] == 70 * 22

def test_calculate_calories_invalid_program(client):
    response = client.post("/calories", json={
        "weight": 70,
        "program": "Invalid"
    })
    assert response.status_code == 400