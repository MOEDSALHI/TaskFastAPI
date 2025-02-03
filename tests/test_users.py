from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.main import app
from app.models.user import User

client = TestClient(app)


def setup_function():
    """Reset the database before each test."""
    Base.metadata.drop_all(bind=engine)  
    Base.metadata.create_all(bind=engine)


def teardown_function():
    """Nettoyer la base de données après chaque test."""
    Base.metadata.drop_all(bind=engine)


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword",
        },
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
