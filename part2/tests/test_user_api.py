import unittest
from app import create_app
import json

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "password": "password"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_data(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email",
            "password": "password"
        })
        self.assertEqual(response.status_code, 400)

    def test_get_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "aaajanedoe@example.com",
            "password": "password"
        })
        
        created_user = json.loads(response.data)
        user_id = created_user['id']
        
        # Get the user
        response = self.client.get(f'/api/v1/users/{user_id}')
        
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_user(self):
        response = self.client.get(f'/api/v1/users/invalid_user_id')        
        self.assertEqual(response.status_code, 404)
    
    def test_update_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "first name",
            "last_name": "last name",
            "email": "user@gmail.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "first name",
            "last_name": "last name",
            "email": "user@hotmail.com"
            })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()