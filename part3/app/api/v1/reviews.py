from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'You have already reviewed this place.')
    @api.response(400, 'You cannot review your own place.')
    @api.response(404, 'User not found')
    @api.response(404, 'Place not found')
    @jwt_required()
    def post(self):
        """Register a new review"""
        current_user = get_jwt_identity()
        if not current_user:
            return {'error': 'Unauthorized action'}, 403

        review_data = api.payload
        place = facade.get_place(review_data["place_id"])
        if not place:
            return {'error': 'Place not found'}, 404
        
        if place.owner_id == current_user:
            return {'error': 'You cannot review your own place.'}, 400

        user = facade.get_user(review_data["user_id"])
        if not user:
            return {'error': 'User not found'}, 404

        if len([item for item in facade.get_all_reviews()
                if item.user_id == review_data["user_id"]
                and item.place_id == review_data["place_id"]]) > 0:
            return {'error': 'You have already reviewed this place.'}, 400

        try:
            new_review = facade.create_review(review_data)
            return {'id': new_review.id, 'text': new_review.text,
                    'rating': new_review.rating,
                    'user_id': new_review.user_id,
                    'place_id': new_review.place_id,
                    }, 201
        except ValueError as e:
            api.abort(400, e)

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [{'id': review.id, 'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id,
                'place_id': review.place_id,
                } for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {'id': review.id, 'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id,
                'place_id': review.place_id,
                }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        current_user = get_jwt_identity()
        is_admin = get_jwt()['is_admin']
        if review.user_id != current_user and not is_admin:
            return {'error': 'Unauthorized action'}, 403

        review_data = api.payload
        try:
            facade.update_review(review_id, review_data)
            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            api.abort(400, e)

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        current_user = get_jwt_identity()
        is_admin = get_jwt()['is_admin']
        if review.user_id != current_user and not is_admin:
            return {'error': 'Unauthorized action'}, 403

        facade.delete_review(review_id) 

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        reviews = facade.get_reviews_by_place(place_id)
        return [{'id': review.id, 'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id,
                'place_id': review.place_id,
                } for review in reviews], 200
