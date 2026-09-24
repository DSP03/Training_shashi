"""
Master Class 5 — Testing
pytest tests for the Notes API, including a mocked dependency.

Run me with:
    pytest -v
"""

from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# ---------------------------------------------------------------------
# Happy-path tests
# ---------------------------------------------------------------------
def test_read_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_get_existing_note():
    resp = client.get("/notes/1")
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == 1
    assert body["title"] == "Welcome"


def test_get_missing_note_returns_404():
    resp = client.get("/notes/9999")
    assert resp.status_code == 404


def test_list_notes_respects_limit():
    resp = client.get("/notes", params={"limit": 1})
    assert resp.status_code == 200
    assert len(resp.json()) == 1


# ---------------------------------------------------------------------
# Validation tests — Pydantic's automatic 422s
# ---------------------------------------------------------------------
def test_create_note_success():
    resp = client.post("/notes", json={
        "title": "My New Note",
        "body": "Some content here.",
        "tags": ["demo"],
    })
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "My New Note"
    assert "id" in body


def test_create_note_blank_title_fails_validation():
    resp = client.post("/notes", json={
        "title": "   ",          # whitespace-only — our custom validator should reject this
        "body": "Some content.",
    })
    assert resp.status_code == 422


def test_create_note_missing_body_fails_validation():
    resp = client.post("/notes", json={"title": "No body here"})
    assert resp.status_code == 422


# ---------------------------------------------------------------------
# Mocking — replacing the "external" call with a stand-in
# ---------------------------------------------------------------------
@patch("main.send_notification")     # like Mockito's @Mock + when(...)
def test_create_note_triggers_notification(mock_send):
    resp = client.post("/notes", json={
        "title": "Triggers a mock",
        "body": "Body text.",
    })
    assert resp.status_code == 201
    mock_send.assert_called_once()   # like verify(mock, times(1))


@patch("main.send_notification")
def test_notification_not_called_on_validation_failure(mock_send):
    resp = client.post("/notes", json={"title": ""})   # fails validation before send_notification runs
    assert resp.status_code == 422
    mock_send.assert_not_called()
