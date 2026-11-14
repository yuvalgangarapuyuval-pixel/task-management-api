import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_add_task(client):
    response = client.post(
        '/tasks',
        json={'title': 'Learn DevOps'}
    )
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
