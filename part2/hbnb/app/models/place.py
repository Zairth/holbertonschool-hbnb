#!/usr/bin/python3
from .base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=[]):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities  # List to store related amenities
        self.reviews = []  # List to store related reviews

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def remove_review(self, review):
        """Remove a review from the list reviews"""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if price < 0:
            raise ValueError("Price must be > 0")
        self.__price = price

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        if not isinstance(latitude, float):
            raise TypeError("Latitude must be a float")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude should be between -90 and 90.")
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        if not isinstance(longitude, float):
            raise TypeError("Longitude must be a float")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude should be between -90 and 90.")
        self.__longitude = longitude