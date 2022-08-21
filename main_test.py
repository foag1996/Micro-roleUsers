import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/roleUsers/H4hR66d7TIuSNju')
    assert response.status_code == 200

def test_204():
    response = client.get('/roleUsers/olshhgdjfbs1')
    assert response.status_code == 204