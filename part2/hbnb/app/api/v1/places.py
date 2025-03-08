from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})


place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Not found')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        if not facade.get_user(place_data['owner_id']):
            return {"error": "ID of the owner not found"}, 404

        if "reviews" in place_data.keys():
            return {"error": "Cannot create a place with a review"}, 400

        new_place = facade.create_place(place_data)

        if "amenities" in place_data:
            amenities = []
            for amenity_data in place_data['amenities']:
                amenity_id = amenity_data['id']
                amenity = facade.get_amenity(amenity_id)
                if amenity:
                    amenities.append({'id': amenity.id, 'name': amenity.name})
                else:
                    return {"error": "Amenity not found"}, 404
            new_place.amenities = amenities

        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id,
            'amenities': new_place.amenities
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        if not places:
            return {'error': 'No place found'}
        return [{'id': place.id, 'title': place.title, 'latitude': place.latitude, 'longitude': place.longitude} for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        user = facade.get_user(place.owner_id)

        return {
            'id': place.id, 
            'title': place.title, 
            'description': place.description, 
            'price': place.price, 
            'latitude': place.latitude, 
            'longitude': place.longitude, 
            'owner': user.to_dict(),
            'amenities': [facade.get_amenity(amenity['id']).to_dict() for amenity in place.amenities],
            'reviews': [review.to_dict() for review in place.reviews]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
        if "owner" in place_data.keys() or "owner_id" in place_data.keys() or "reviews" in place_data.keys():
            return {'error': 'Invalid input data, forbidden access'}, 400

        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        facade.update_place(place.id, place_data)

        return {"message": "Place updated successfully"}, 200
