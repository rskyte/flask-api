import sys
sys.path.append("./")

import pytest

from api import app

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_app_route_returns_ok_status_code(client):
    response = client.get("/")
    assert response.status_code == 200