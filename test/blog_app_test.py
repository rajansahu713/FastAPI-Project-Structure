import json

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from database.db import Base, get_db
from main import app

client = TestClient(app)

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def test_data():
    with open("test/test_data.json") as f:
        return json.load(f)


def test_register_user(test_data):
    test_user = test_data["user_credentials"]
    response = client.post("/auth/register", json=test_user)
    assert response.status_code == 200
    assert response.json()["username"] == "string"


def test_generate_token(test_data):
    response = client.post(
        "/auth/token",
        data={
            "username": test_data["user_credentials"]["username"],
            "password": test_data["user_credentials"]["password"],
        },
    )
    assert response.status_code == 200
    test_data["token"] = response.json()["access_token"]
    with open("test/test_data.json", "w") as f:
        json.dump(test_data, f, indent=4)
    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_create_blog(test_data):
    token = test_data["token"]
    test_blog = {"title": "string", "description": "string"}
    response = client.post(
        "/blogs", json=test_blog, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Blog created successfully"


def test_get_blog(test_data):
    token = test_data["token"]
    response = client.get("/blogs/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()) > 0


def teardown_module(module):
    Base.metadata.drop_all(bind=engine)
