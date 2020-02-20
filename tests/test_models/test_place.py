#!/usr/bin/python3
"""Place tests"""


from models.place import Place
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestPlace (TestBase):
    """Place tests"""

    def __init__(self, *args, **kwargs):
        """Place tests"""

        super().__init__(*args, **kwargs)
        self._cls = Place
        self._name = 'Place'

    def test_permissions(self):
        """Place tests"""
        is_read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """Place tests"""
        my_place = Place()
        self.assertIsInstance(my_place, Place)
