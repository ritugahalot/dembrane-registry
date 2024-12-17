import os
from urllib.parse import quote_plus
from mongomock import Database, MongoClient
import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock
from app.database import db

@pytest.fixture(autouse=True)
def mock_db():
    db = get_db()
    yield db
    db.forms = MagicMock()
    db.responses = MagicMock()

@pytest.fixture
def client():
    return TestClient(app)

def get_db() -> Database:
    """
    Get the database

    Returns:
        Database: The Database handle
    """
    url = os.getenv("DATABASE_URL", "")
    username = os.getenv("DATABASE_USERNAME", "")
    password = os.getenv("DATABASE_PASSWORD", "")
    db_name = os.getenv("DATABASE_NAME", "")
    uri = f"mongodb://{username}:{password}@{quote_plus(url)}/{db_name}"
    client = MongoClient(uri, tlsInsecure=True)
    db = client[db_name]
    return db