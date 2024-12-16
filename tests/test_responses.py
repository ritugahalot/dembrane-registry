def test_submit_response(client, mock_db):
    form_id = "mocked_form_id"
    response_data = {
        "form_id": form_id,
        "answers": [
            {"question": "What is your name?", "response": "John Doe"},
            {"question": "Favorite color?", "response": "Blue"}
        ]
    }

    mock_db.forms.find_one.return_value = {"_id": form_id}

    mock_db.responses.insert_one.return_value.inserted_id = "mocked_response_id"

    response = client.post("/api/responses", json=response_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Responses submitted successfully"}

def test_submit_response_form_not_found(client, mock_db):
    form_id = "non_existent_form_id"
    response_data = {
        "form_id": form_id,
        "answers": [
            {"question": "What is your name?", "response": "John Doe"},
            {"question": "Favorite color?", "response": "Blue"}
        ]
    }

    mock_db.forms.find_one.return_value = None

    response = client.post("/api/responses", json=response_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Form not found"}

def test_get_responses(client, mock_db):
    form_id = "mocked_form_id"
    mock_responses = [
        {
            "_id": "response_id_1",
            "form_id": form_id,
            "answers": [
                {"question": "What is your name?", "response": "John Doe"},
                {"question": "Favorite color?", "response": "Blue"}
            ]
        },
        {
            "_id": "response_id_2",
            "form_id": form_id,
            "answers": [
                {"question": "What is your name?", "response": "Jane Smith"},
                {"question": "Favorite color?", "response": "Red"}
            ]
        }
    ]

    # Mock database query
    mock_db.responses.find.return_value = mock_responses

    response = client.get(f"/api/responses/{form_id}")
    assert response.status_code == 200
    assert response.json() == {
        form_id: [
            [
                {"question": "What is your name?", "response": "John Doe"},
                {"question": "Favorite color?", "response": "Blue"}
            ],
            [
                {"question": "What is your name?", "response": "Jane Smith"},
                {"question": "Favorite color?", "response": "Red"}
            ]
        ]
    }
