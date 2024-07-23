import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert b'Search' in rv.data

def test_xss_attack(client):
    rv = client.post('/', data=dict(search_term='<script>alert(1)</script>'))
    assert b'XSS attack detected' in rv.data

def test_sql_injection(client):
    rv = client.post('/', data=dict(search_term='SELECT * FROM users'))
    assert b'SQL injection detected' in rv.data

def test_valid_search(client):
    rv = client.post('/', data=dict(search_term='safe search'))
    assert b'Search term: safe search' in rv.data
