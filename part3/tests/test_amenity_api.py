import unittest
from app import create_app
import json

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "user",
            "last_name": "amenity",
            "email": "user_amenity@example.com",
            "password": "password",
            "is_admin": True
        })

        response = self.client.post('/api/v1/auth/login', json={
            "email": "user_amenity@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        
        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 1",
        }, headers=access_headers)
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "user",
            "last_name": "amenity",
            "email": "user_amenity1@example.com",
            "password": "password",
            "is_admin": True
        })

        response = self.client.post('/api/v1/auth/login', json={
            "email": "user_amenity1@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}
        response = self.client.post('/api/v1/amenities/', json={
            'name': '',
        }, headers=access_headers)
        self.assertEqual(response.status_code, 400)

    def test_get_amenity(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "user",
            "last_name": "amenity",
            "email": "user_amenity2@example.com",
            "password": "password",
            "is_admin": True
        })

        response = self.client.post('/api/v1/auth/login', json={
            "email": "user_amenity2@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}

        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 2",
        }, headers=access_headers)
        created_amenity = json.loads(response.data)
        amenity_id = created_amenity['id']
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_amenity(self):
        response = self.client.get(f'/api/v1/amenities/invalid_amenity_id')        
        self.assertEqual(response.status_code, 404)
    
    def test_update_amenity(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "user",
            "last_name": "amenity",
            "email": "user_amenity4@example.com",
            "password": "password",
            "is_admin": True
        })

        response = self.client.post('/api/v1/auth/login', json={
            "email": "user_amenity4@example.com",
            "password": "password"})
        access_token = response.get_json()["access_token"]
        access_headers = {"Content-Type":"application/json", "accept":"application/json","Authorization": "Bearer {}".format(access_token)}

        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 3",
        }, headers=access_headers)
        created_amenity = json.loads(response.data)
        amenity_id = created_amenity['id']
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            'name': 'amenity 4',
            }, headers=access_headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()