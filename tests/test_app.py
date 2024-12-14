import pytest
from main import app  

@pytest.fixture
def client():
    return app.test_client()

def test_noquery(client):
    response = client.get('/process_search')
    assert response.status_code == 400
    assert response.json == {"message": "Invalid Query parameter", "results": []}

def test_invalidquery(client):
    response = client.get('/process_search?q=ab')
    assert response.status_code == 400
    assert response.json == {"message": "Invalid Query parameter", "results": []}

def test_nomatch(client):
    response = client.get('/process_search?q=xyz')
    assert response.status_code == 404
    assert response.json == {"message":"No results found", "results":[]}

def test_match(client):
    response = client.get('/process_search?q=sur') 
    assert response.status_code == 200
    results = response.json.get("results", [])
    assert len(results) <= 10 
    for result in results:
        assert "name" in result
        assert result["name"].lower().startswith("sur")

