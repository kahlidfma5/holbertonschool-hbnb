from flask_restx import Namespace, Resource, fields
from app.services import facade


api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, min_length = 1, max_length = 50, description='Name of the amenity'),
})


@api.route('/')
class AmenityList(Resource):
    '''Shows a list of all amenities, and lets you POST to add new amenities'''
    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        '''List all Amenities'''
        return facade.get_all_amenities()

    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        '''Create a new amenity'''
        return facade.create_amenity(api.payload), 201

@api.response(200, 'List of amenities retrieved successfully')
def get(self):
    """Retrieve a list of all amenities"""
    amenities = facade.get_all_amenities()
    return {'amenities': [{'id': amenity.id, 'name': amenity.name} for amenity in amenities]}, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return {'id': amenity.id, 'name': amenity.name}, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        """
        amenity = facade.get_amenity(amenity_id)

        if not amenity:
            return {'error': 'Amenity not found'}, 404
        if not amenity_data['name']:
            return {'error': 'Amenity name should have a value'}, 400
        if len(amenity_data['name']) <= 1 and len(amenity_data['name']) > 50 :
            return {'error': 'The maximum length of the amenity name is 50 characters'}, 400
        """
        facade.update_amenity(amenity_id, amenity_data)
        return {"message": "Amenity updated successfully"}, 200
