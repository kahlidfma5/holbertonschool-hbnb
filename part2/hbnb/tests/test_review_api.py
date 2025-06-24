import unittest
from app import create_app
import json

class TestReviewEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_review(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janeaa_qdoe@example.com"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            })
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': user_id,
            'place_id': place_id
            })
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@example.com"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            })
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': 'invalid_user_id',
            'place_id': place_id
            })
        self.assertEqual(response.status_code, 404)

    def test_create_review_invalid_place(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoabc_tee@example.com"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            })
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': user_id,
            'place_id': 'invalid_place_id'
            })
        self.assertEqual(response.status_code, 404)

    def test_get_review(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane_adoe@example.com"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            })
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': user_id,
            'place_id': place_id
            })

        created_review = json.loads(response.data)
        review_id = created_review['id']
        response = self.client.get(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 200)
    
    def test_get_invalid_review(self):
        response = self.client.get(f'/api/v1/reviews/invalid_place_id')        
        self.assertEqual(response.status_code, 404)
    
    def test_update_review(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane_yu7adoe@example.com"
        })
        created_user = json.loads(response.data)
        user_id = created_user['id']
        response = self.client.post('/api/v1/places/', json={
            'title': 'title',
            'description': 'description',
            'price': 100,
            'latitude': 40,
            'longitude': 100,
            'owner_id': user_id,
            })
        created_place = json.loads(response.data)
        place_id = created_place['id']
        response = self.client.post('/api/v1/reviews/', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': user_id,
            'place_id': place_id
            })

        created_review = json.loads(response.data)
        review_id = created_review['id']
        response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "dummy text",
            'rating': 1,
            'user_id': user_id,
            'place_id': place_id
            })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()