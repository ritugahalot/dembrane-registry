import pytest
from fastapi.testclient import TestClient
from app.main import registry
from unittest.mock import MagicMock
from app.database import db

@pytest.fixture(autouse=True)
def mock_db():
    db.forms = MagicMock()
    db.responses = MagicMock()

@pytest.fixture
def client():
    return TestClient(registry)
