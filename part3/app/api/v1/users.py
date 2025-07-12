from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
})
user_model = api.inherit('User', user_update_model, {
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description="User's passowrd")
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
        except ValueError as e:
            api.abort(400, e)

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @api.expect(user_update_model, validate=True)
    @jwt_required()
    def put(self, user_id):
        """Update a users's information"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        current_user = get_jwt_identity()
        is_admin = get_jwt()['is_admin']
        api.logger.info(f"{is_admin}")

        if is_admin:
            api.logger.info("True")
        else:
            api.logger.info("False")
        
        if not current_user:
            return {'error': 'Unauthorized action'}, 403

        if user_id != current_user and not is_admin:
            return {'error': 'Unauthorized action'}, 403
        
        if is_admin:
            api.expect(user_model)

        user_data = api.payload
        if not is_admin and (user_data.get("email") or user_data.get("password")):
            return {'error': 'Email or password cannot be updated. Call Admin'}, 400
        try:
            facade.update_user(user_id, user_data)
            return {"message": "User updated successfully"}, 200
        except ValueError as e:
            api.abort(400, e)
