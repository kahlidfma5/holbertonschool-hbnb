import unittest
from app import create_app
import json

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 1",
        })
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid_name(self):
        response = self.client.post('/api/v1/amenities/', json={
            'name': '',
        })
        self.assertEqual(response.status_code, 400)

    def test_get_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 2",
        })
        created_amenity = json.loads(response.data)
        amenity_id = created_amenity['id']
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_amenity(self):
        response = self.client.get(f'/api/v1/amenities/invalid_amenity_id')        
        self.assertEqual(response.status_code, 404)
    
    def test_update_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "amenity 3",
        })
        created_amenity = json.loads(response.data)
        amenity_id = created_amenity['id']
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            'name': 'amenity 4',
            })
        self.assertEqual(response.status_code, 200)
    


if __name__ == '__main__':
    unittest.main()