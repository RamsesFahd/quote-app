from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Quotidian" in response.data

def test_api_quote():
    client = app.test_client()
    response = client.get("/api/quote")
    assert response.status_code == 200

def test_api_quote_with_category():
    client = app.test_client()
    response = client.get("/api/quote?category=motivation")
    assert response.status_code == 200

def test_api_quote_unknown_category_falls_back():
    client = app.test_client()
    response = client.get("/api/quote?category=xyz123")
    assert response.status_code == 200