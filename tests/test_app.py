"""
Unit tests for the Flask application
"""
import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    app.config['ENVIRONMENT'] = 'test'
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data
    assert 'environment' in data


def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data


def test_get_users(client):
    """Test getting all users"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_create_user(client):
    """Test creating a new user"""
    user_data = {
        'name': 'Test User',
        'email': 'test@example.com'
    }
    response = client.post('/api/users', json=user_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test User'
    assert data['email'] == 'test@example.com'


def test_create_user_missing_fields(client):
    """Test creating user with missing fields"""
    response = client.post('/api/users', json={'name': 'Test'})
    assert response.status_code == 400


def test_get_user_by_id(client):
    """Test getting user by ID"""
    response = client.get('/api/users/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1


def test_get_user_not_found(client):
    """Test getting non-existent user"""
    response = client.get('/api/users/999')
    assert response.status_code == 404

