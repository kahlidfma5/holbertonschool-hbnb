import unittest
from app import create_app
import json


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane_doe@example.com",
            "password": "password"
        })
        print(f'Create Place User Response: {response.get_json()}')
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/auth/login', json={
            "email": "jane_doe@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}

        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            }, headers=access_headers)
        self.assertEqual(response.status_code, 201)

    def test_get_place(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janexdoe@example.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        print(f'Created user ID: {user_id}')
        
        response = self.client.post('/api/v1/auth/login', json={
            "email": "janexdoe@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}

        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            }, headers=access_headers)
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.get(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_place(self):
        response = self.client.get('/api/v1/places/invalid_place_id')        
        self.assertEqual(response.status_code, 404)
    
    def test_update_place(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "ajanexdoe@example.com",
            "password": "password"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/auth/login', json={
            "email": "ajanexdoe@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            }, headers=access_headers)

        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.put(f'/api/v1/places/{place_id}', json={
            'title': 'title 1',
            'description': 'description 1',
            'price': 10,
            'latitude': 30,
            'longitude': 120,
            'owner_id': user_id,
            }, headers=access_headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()