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
