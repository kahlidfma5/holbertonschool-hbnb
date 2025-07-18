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

    def test_create_admin_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin@example.com",
            "password": "password",
            "is_admin": 1
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
            "email": "user1@gmail.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        
        response = self.client.post('/api/v1/auth/login', json={
            "email": "user1@gmail.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "first name1",
            "last_name": "last name1"
            }, headers=access_headers)
        self.assertEqual(response.status_code, 200)

    def test_update_user_with_email(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "first name",
            "last_name": "last name",
            "email": "user3@gmail.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        
        response = self.client.post('/api/v1/auth/login', json={
            "email": "user3@gmail.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "first name1",
            "last_name": "last name1",
            "email": "user4@gmail.com"
            }, headers=access_headers)
        self.assertEqual(response.status_code, 400)

    def test_update_user_by_admin(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "first name",
            "last_name": "last name",
            "email": "user2@gmail.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        
        response = self.client.post('/api/v1/users/', json={
            "first_name": "first name",
            "last_name": "last name",
            "email": "admin2@gmail.com",
            "password": "password",
            "is_admin": True
        })
        # created_admin_user = json.loads(response.data)
        # user_admin_id = created_user['id']

        response = self.client.post('/api/v1/auth/login', json={
            "email": "admin2@gmail.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        
        response = self.client.put(f'/api/v1/users/{user_id}', json={
            "first_name": "first name2",
            "last_name": "last name2",
            "email": "user22@gmail.com",
            "password": "password1"
            }, headers=access_headers)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()