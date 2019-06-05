import os
import sys
import pytest
import unittest
sys.path.append("./")
sys.path.append(os.getcwd() + "/src")

from api import create_app
from unittest.mock import MagicMock
from s3_logic import S3Logic

@pytest.fixture
def app():
    s3 = S3Logic()
    s3.get_all_user_ids = MagicMock(return_value=[])
    s3.put = MagicMock(return_value=200)
    app = create_app(s3)
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
    assert response.data == b'<h1>Flask API<h1>'

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
    assert response.get_json()["users"] == []