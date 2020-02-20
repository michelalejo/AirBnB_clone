#!/usr/bin/python3
"""User tests"""


from models.amenity import Amenity
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestAmenity (TestBase):
    """Amenity tests"""

    def __init__(self, *args, **kwargs):
        """Amenity tests"""

        super().__init__(*args, **kwargs)
        self._cls = Amenity
        self._name = 'Amenity'

    def test_permissions(self):
        """Amenity tests"""
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """Amenity tests"""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
