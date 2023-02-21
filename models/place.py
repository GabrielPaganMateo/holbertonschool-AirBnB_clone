#!/usr/bin/python3
"""Module provide User class"""
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """User class that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
        self.city_id = City.id
        self.user_id = User.id
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = Amenity.id