import json

from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from database.db import Base, get_db
from main import app

client = TestClient(app)

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
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


def test_register_user():
    with open("test/test_data.json") as f:
        test_data = json.load(f)
    test_user = test_data["user_credentials"]
    response = client.post("/auth/register", json=test_user)
    assert response.status_code == 200
    assert response.json()["username"] == "string"


def test_generate_token():
    # Generate a token for the test user
    with open("test/test_data.json") as f:
        test_data = json.load(f)

    response = client.post(
        "/auth/token",
        data={
            "username": test_data["user_credentials"]["username"],
            "password": test_data["user_credentials"]["password"],
        },
    )
    assert response.status_code == 200
    # save the generated token to json file
    with open("test/test_data.json", "w") as f:
        test_data["token"] = response.json()["access_token"]
        json.dump(test_data, f)
    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_create_blog():
    # Create a test blog
    with open("test/test_data.json") as f:
        test_data = json.load(f)

    token = test_data["token"]

    test_blog = {"title": "string", "description": "string"}
    response = client.post(
        "/blogs", json=test_blog, headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Blog created successfully"


def test_get_blog():
    with open("test/test_data.json") as f:
        test_data = json.load(f)

    token = test_data["token"]

    response = client.get("/blogs/", headers={"Authorization": f"Bearer {token}"})
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def teardown() -> None:
    Base.metadata.drop_all(bind=engine)
