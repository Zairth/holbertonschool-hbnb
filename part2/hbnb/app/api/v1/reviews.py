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
    def post(self):
        """Register a new review"""
        review_data = api.payload

        try:
            place = facade.get_place(review_data['place_id'])
            if not place:
                return {"error": "Place not found, cannot add review"}, 404

            id_user = review_data['user_id']

            if place.owner_id == id_user:
                return {'error': 'Cannot add a review for your own place'}, 400

            new_review = facade.create_review(review_data)
            place.add_review(new_review)
        except Exception as e:
            return {"error": str(e)}, 404
        
        return {'id': new_review.id, 'text': new_review.text, 'rating': new_review.rating, 'user_id': new_review.user_id, 'place_id': place.id}, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        if not reviews:
            return {'error': 'No review found'}
        return [{'id': review.id, 'text': review.text, 'rating': review.rating} for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {'id': review.id, 'text': review.text, 'rating': review.rating, 'user_id': review.user_id, 'place_id': review.place_id}, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review_data = api.payload

        if "id" in review_data.keys():
            return {"error": "Cannot update the ID of the Review"}, 400

        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        place = facade.get_place(review.place_id)
        if not place:
            return {"error": "Place not found"}, 404
        if place.id != review_data['place_id']:
            return {"error": "Wrong place_id input"}, 404

        if review_data['user_id'] != review.user_id:
            return {'error': 'Cannot update review that is not yours'}, 400

        facade.update_review(review_id, review_data)

        return {"message": "Review updated successfully"}, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):

        review = facade.get_review(review_id)
        if not review:
            return{'error': 'Review not found'}, 404

        place = facade.get_place(review.place_id)
        place.remove_review(review)
        facade.delete_review(review_id)

        return{"message": "Review deleted"}, 200
        

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews in this place"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        reviews = place.reviews
        if not reviews:
            return {'error': 'No reviews existant'}
        return [{'id': review.id, 'text': review.text, 'rating': review.rating} for review in reviews], 200