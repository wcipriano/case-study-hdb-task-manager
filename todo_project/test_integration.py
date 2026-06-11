import pytest
from todo_app import app, db

@pytest.fixture
def client():
    with app.app_context():
        yield app.test_client()

def test_pagina_inicial(client):
    response = client.get('/')
    assert response.status_code == 200, "Expected status code 200 (OK)"
    assert 'Task Manager' in response.data.decode('utf-8'), "Response should contain app name"

def test_pagina_login(client):
    response = client.get('/login')
    assert response.status_code == 200, "Expected status code 200 (OK)"
    assert 'Username' in response.data.decode('utf-8'), "Response should contain label Username"
    assert 'Password' in response.data.decode('utf-8'), "Response should contain label Password"
