from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
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
            return {'error': 'Email already used'}, 400

        new_user = facade.create_user(user_data)
        return new_user.to_dict(), 201

    @api.response(200, 'Users successfully retrieved')
    @api.response(404, 'No users found')
    def get(self):
        """Get all the users"""
        users = facade.get_all_users()
        if not users:
            return {'error': 'No users found'}, 404
        return users, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return user.to_dict(), 200

    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Input data invalid')
    def put(self, user_id):
        """Update a specific user"""
        user_data = api.payload
        user = facade.get_user(user_id)

        if not user:
            return {'error': 'User not found'}, 404
        
        if "id" in user_data.keys():
            return {'error': 'Input data invalid'}, 400

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            if user_id != existing_user.id:
                return {"error": "email is already used."}, 409

        updated_user = facade.update_user(user_id, user_data)

        return updated_user.to_dict(), 200
