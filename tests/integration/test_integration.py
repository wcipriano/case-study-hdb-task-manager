def test_pagina_inicial(test_client):
    response = test_client.get('/')
    assert response.status_code == 200, "Expected status code 200 (OK)"
    assert 'Task Manager' in response.data.decode('utf-8'), "Response should contain app name"

def test_pagina_login(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200, "Expected status code 200 (OK)"
    assert 'Username' in response.data.decode('utf-8'), "Response should contain label Username"
    assert 'Password' in response.data.decode('utf-8'), "Response should contain label Password"
