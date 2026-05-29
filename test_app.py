import json
from app import app

app.config['TESTING'] = True


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Anime Quotes" in response.data


def test_api_quote():
    client = app.test_client()
    response = client.get("/api/quote")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "quote" in data
    assert "character" in data
    assert "category" in data


def test_api_quote_with_category():
    client = app.test_client()
    response = client.get("/api/quote?category=motivation")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["category"] == "motivation"
    assert data["character"]["name"] == "Sakura"


def test_api_quote_unknown_category_falls_back():
    client = app.test_client()
    response = client.get("/api/quote?category=nonexistent")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "quote" in data
