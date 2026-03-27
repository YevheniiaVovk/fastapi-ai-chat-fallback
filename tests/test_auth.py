from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    # Перевіряємо, чи працює головна сторінка або swagger
    response = client.get("/docs")
    assert response.status_code == 200


def test_registration_flow():
    # Додаємо username, бо схема UserCreate його вимагає
    payload = {
        "email": "test_new_user@example.com", 
        "password": "password123",
        "username": "test_warrior"
    }
    response = client.post("/auth/registration", json=payload)
    
    # Тепер він має повернути 200/201 (якщо новий) або 400 (якщо вже існує)
    assert response.status_code in [200, 201, 400]