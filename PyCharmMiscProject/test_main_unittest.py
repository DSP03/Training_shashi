"""
Master Class 5 — Testing
The SAME core tests as test_main.py, written in the class-based
unittest style — the one that feels most familiar coming from JUnit.

Run me with:
    python -m unittest test_main_unittest.py -v
    (or just: pytest test_main_unittest.py -v — pytest can run unittest too)
"""

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


class TestNotesAPI(unittest.TestCase):

    def setUp(self):                     # like JUnit's @BeforeEach
        self.client = TestClient(app)

    def test_read_root(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"status": "ok"})

    def test_get_existing_note(self):
        resp = self.client.get("/notes/1")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["title"], "Welcome")

    def test_get_missing_note_returns_404(self):
        resp = self.client.get("/notes/9999")
        self.assertEqual(resp.status_code, 404)

    def test_create_note_blank_title_fails_validation(self):
        resp = self.client.post("/notes", json={"title": "   ", "body": "x"})
        self.assertEqual(resp.status_code, 422)

    @patch("main.send_notification")
    def test_create_note_triggers_notification(self, mock_send):
        resp = self.client.post("/notes", json={"title": "Hi", "body": "there"})
        self.assertEqual(resp.status_code, 201)
        mock_send.assert_called_once()


if __name__ == "__main__":
    unittest.main()
