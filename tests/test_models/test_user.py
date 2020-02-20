#!/usr/bin/python3
"""User tests"""


from models.user import User
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestUser(TestBase):
    """User tests"""

    def __init__(self, *args, **kwargs):
        """User tests"""

        super().__init__(*args, **kwargs)
        self._cls = User
        self._name = 'User'

    def test_permissions(self):
        """User tests"""
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """User tests"""
        my_user = User()
        self.assertIsInstance(my_user, User)
