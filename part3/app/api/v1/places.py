from flask_cors import cross_origin
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),

})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def post(self):
        """Register a new Place"""

        current_user = get_jwt_identity()
        if not current_user:
            return {'error': 'Unauthorized action'}, 403

        place_data = api.payload

        try:
            new_place = facade.create_place(place_data)
            return {'id': new_place.id, 'title': new_place.title,
                    'description': new_place.description,
                    'price': new_place.price,
                    'latitude': new_place.latitude,
                    'longitude': new_place.longitude,
                    'owner_id': current_user
                    }, 201
        except ValueError as e:
            api.abort(400, e)

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{'id': place.id, 'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id,
                'reviews':[{"id": review.id, "text": review.text,
                            "rating": review.rating,
                            "user_id": review.user_id,
                            "user_name": f"{review.user.first_name} {review.user.last_name}"}
                            for review in place.reviews ]
                } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        reviews = facade.get_reviews_by_place(place_id)
        return {'id': place.id, 'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id,
                'reviews': [{'id': review.id, 'text': review.text,
                             'rating': review.rating,
                             'user_id': review.user_id,
                             'place_id': review.place_id,
                             } for review in reviews]
                }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        current_user = get_jwt_identity()
        is_admin = get_jwt()['is_admin']
        if place.owner_id != current_user and not is_admin:
            return {'error': 'Unauthorized action'}, 403

        place_data = api.payload
        try:
            facade.update_place(place_id, place_data)
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            api.abort(400, e)