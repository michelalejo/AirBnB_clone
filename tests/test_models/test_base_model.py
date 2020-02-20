#!/usr/bin/python3
"""Tests for Base Model"""

import unittest
import json
import pep8
from os import path
import os
from models.base_model import BaseModel


class Testpep8(unittest.TestCase):
    """Pep8 testing"""

    def test_pep8(self):
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        FileBase_Model = "models/base_model.py"
        FileBase_ModelTest = "tests/test_models/test_base_model.py"
        check = style.check_files([FileBase_Model, FileBase_ModelTest])
        self.assertEqual(check.total_errors, 0, msg)


class TestBase(unittest.TestCase):
    """ Test all of i think """

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def TestModels(self):
        """Test model name"""
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')
        """Test model numbers"""
        self.my_model.my_number = 55
        self.assertEqual(self.my_model.my_number, 55)
        """Test model exist"""
        self.assertTrue(path.isfile('my_file.json'))
        """Test model to dict"""
        model = self.my_model.to_dict()
        self.assertIsInstance(model["created_at"], str)
        self.assertIsInstance(model["updated_at"], str)
        self.assertIsInstance(model["my_number"], int)
        self.assertIsInstance(model["id"], str)

    def test_permissions(self):
        """Test BaseModel Permissions"""

        test_file = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

if __name__ == '__main__':
    unittest.main()
