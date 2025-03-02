#!/usr/bin/python3
from .base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) > 50:
            raise ValueError("Too many characters")
        super().__init__()
        self.name = name
