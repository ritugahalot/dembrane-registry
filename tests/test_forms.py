import pytest

def test_create_form(client, mock_db):
    form_data = {
        "title": "Test Form",
        "questions": [
            {"type": "text", "prompt": "What is your name?"},
            {"type": "multiple-choice", "prompt": "Favorite color?", "options": ["Red", "Blue"]}
        ]
    }

    mock_db.forms.insert_one.return_value.inserted_id = "mocked_id"

    response = client.post("/api/forms", json=form_data)
    assert response.status_code == 200
    assert response.json() == {"formId": "mocked_id"}

def test_get_form(client, mock_db):
    form_id = "mocked_form_id"
    form_data = {
        "_id": form_id,
        "title": "Test Form",
        "questions": [
            {"type": "text", "prompt": "What is your name?"},
            {"type": "multiple-choice", "prompt": "Favorite color?", "options": ["Red", "Blue"]}
        ]
    }

    mock_db.forms.find_one.return_value = form_data

    response = client.get(f"/api/forms/{form_id}")
    assert response.status_code == 200
    assert response.json() == form_data

def test_get_form_not_found(client, mock_db):
    form_id = "non_existent_id"
    mock_db.forms.find_one.return_value = None

    response = client.get(f"/api/forms/{form_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Form not found"}
