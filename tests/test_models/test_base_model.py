#!/usr/bin/python3
"""Tests for Base Model"""


from models.base_model import BaseModel
import unittest
import json
import pep8
import unittest


class Testpep8(unittest.TestCase):
    """Pep8 testing"""
    def test_pep8(self):
        msg = "Found code style errors (and warning)."
        style = pep8.StyleGuide(quiet=True)
        FileBase_Model = "models/base_model.py"
        FileBase_ModelTest = "tests/test_models/test_base_model.py"
        check = style.check_files([FileBase_Model, FileBase_ModelTest])
        self.assertEqual(check.total_errors, 0, msg)

    def id_unique(self):
        """"Id testing"""

        id_u = self._cls()
        with self.subTest(msg='id is a UUID'):
            self.assertIsInstance(id_u.id, str)
            self.assertIsInstance(uuid.UUID(id_u.id), uuid.UUID)
        with self.subTest(msg='IDs are unique'):
            self.assertNotEqual(self.__class__().id, self.__class__().id)
