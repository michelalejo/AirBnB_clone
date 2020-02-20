#!/usr/bin/python3
"""User tests"""


from models.user import User
from tests.test_models.test_base_model import TestBase


class TestUser (TestBase):
    """User tests"""

    def __init__(self, *args, **kwargs):
        """User tests"""

        super().__init__(*args, **kwargs)
        self._cls = User
        self._name = 'User'

    def test_is_an_instance(self):
        """User tests"""
        my_user = User()
        self.assertIsInstance(my_user, User)
