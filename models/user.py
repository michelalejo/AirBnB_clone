#!/usr/bin/python3
""" Write a class User that inherits from BaseModel: """
from models.base_model import BaseModel


class User(BaseModel):
    """ Write a class User that inherits from BaseModel: """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
