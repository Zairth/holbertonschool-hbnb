from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_datas = api.payload

        if not amenity_datas:
            return {'error': 'Invalid input data'}, 400

        if len(amenity_datas['name']) <= 0:
            return {'error': 'Name can\'t be empty'}, 400

        new_amenity = facade.create_amenity(amenity_datas)

        return {"id": new_amenity.id, "name": new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities_list = facade.get_all_amenities()
        return [{"id": amenity.id, "name": amenity.name} for amenity in amenities_list], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        return {"id": amenity.id, "name": amenity.name}, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = api.payload
        amenity = facade.get_amenity(amenity_id)

        if not data:
            return {"error": "Invalid input data"}, 400
        if not amenity:
            return {"error": "Amenity not found"}, 404
        if len(data['name']) <= 0:
            return {'error': 'Name can\'t be empty'}, 400

        new_amenity = facade.update_amenity(amenity_id, data)

        return {"message": "Amenity updated successfully"}, 200