#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel

name = ""


class State(BaseModel):
    """ State class """

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
