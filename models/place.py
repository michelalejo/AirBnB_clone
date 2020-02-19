#!/usr/bin/python3
""" class place """
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity

city_id = City.id
user_id = User.id
name = ""
description = ""
number_rooms = 0
number_bathrooms = 0
max_guest = 0
price_by_night = 0
latitude = 0.0
longitude = 0.0
amenity_ids = Amenity.id


class Place(BaseModel):
    """ Place class """

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
