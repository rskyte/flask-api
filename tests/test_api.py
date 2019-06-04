import os
import sys
sys.path.append("./")
sys.path.append(os.getcwd() + "/flask-api")

print(sys.path)
print(os.getcwd())

import pytest

from src.api import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    client = app.test_client()
    return client

def test_app_route_returns_ok_status_code(client):
    response = client.get("/")
    assert response.status_code == 200