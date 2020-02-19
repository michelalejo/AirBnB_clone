#!/usr/bin/python3
""" class amenity """
from models.base_model import BaseModel

name = ""


class Amenity(BaseModel):
    """ Amenity class """

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
