import pytest
from firstApp import app

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client

def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.get_json() == {'message': 'pong'}

def test_echo(client):
    res = client.get('/echo?msg=hello')
    assert res.status_code == 200
    assert res.get_json() == {'echo': 'hello'}

def test_multiply(client):
    res = client.get('/multiply/2/3')
    assert res.get_json() == {'result': 6}

def test_json_endpoint(client):
    res = client.post('/json', json={'foo': 'bar'})
    assert res.get_json() == {'you_sent': {'foo': 'bar'}}

def test_form_endpoint(client):
    res = client.post('/form', data={'name': 'Alice'})
    assert res.get_json() == {'form_data': {'name': 'Alice'}}
