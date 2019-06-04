import os
import sys
import pytest
sys.path.append("./")
sys.path.append(os.getcwd() + "/src")

from api import create_app

@pytest.fixture
def app():
    print("In App")
    app = create_app()
    return app

@pytest.fixture
def client(app):
    client = app.test_client()
    return client

def test_api_route_returns_ok_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

def test_api_route_has_welcome_page(client):
    response = client.get("/")
    assert response.data == "<h1>Flask API<h1>"

def test_api_can_receive_user_data(client):
    test_data = {'userId': 'jbloggs', 'name': 'Joseph Bloggs'}
    response = client.post("/api/users", json=test_data)
    assert response.status_code == 200
    assert response.data == "User: jbloggs, created."