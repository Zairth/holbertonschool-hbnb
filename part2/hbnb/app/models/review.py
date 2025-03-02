#!/usr/bin/python3
from .base_model import BaseModel
from .user import User
from .place import Place


def verify_instance(text, rating, place_id, user_id):
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(rating, int):
        raise TypeError("Rating must be an integer")
    # if not isinstance(place_id, Place):
    #     raise TypeError("Place must be a Class of Place")
    # if not isinstance(user_id, User):
    #     raise TypeError("User must be a class of User")

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        verify_instance(text, rating, place_id, user_id)
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'user_id': self.user_id
        }
