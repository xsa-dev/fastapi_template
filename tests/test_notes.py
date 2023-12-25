import unittest
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"
        self.email = "test@gmail.com"
        self.token = None
        self.note_id = None
    
    def test_create_user(self):
        response = requests.post(
            "http://localhost:8000/api/v1/users/",
            json={"username": self.username, "password": self.password, "email": self.email},
        )
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = requests.post(
            "http://localhost:8000/api/v1/login/",
            auth=(self.username, self.password),
        )
        self.token = response.json()["access_token"]
        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        response = requests.post(
            "http://localhost:8000/api/v1/notes/",
            json={"text": "Test note"},
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.note_id = response.json()["id"]

    def test_edit_note(self):
        response = requests.put(
            f"http://localhost:8000/api/v1/notes/{self.note_id}",
            json={"text": "Edited note"},
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_get_notes(self):
        response = requests.get(
            "http://localhost:8000/api/v1/notes",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_note(self):
        response = requests.delete(
            f"http://localhost:8000/api/v1/notes/{self.note_id}",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()