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
    value = response.data
    assert value == "<h1>Flask API<h1>"

def test_api_can_receive_user_data(client):
    test_data = {'userId': 'jbloggs', 'name': 'Joseph Bloggs'}
    response = client.post("/api/users", json=test_data)
    assert response.status_code == 200
    assert response.get_json() == {'status': 'success', 'userId': 'jbloggs'}

def test_api_refuses_data_in_incorrect_format(client):
    response = client.post("/api/users", json="incorrect")
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Please provide data in correct format'}

def test_api_can_return_all_users(client):
    response = client.get("/api/users/all")
    assert response.status_code == 200
    assert type(response.get_json()["users"]) == list