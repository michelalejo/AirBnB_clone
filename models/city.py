#!/usr/bin/python3
""" class city """
from models.base_model import BaseModel
from models.state import State

state_id = State.id
name = ""


class City(BaseModel):
    """ City class """

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
