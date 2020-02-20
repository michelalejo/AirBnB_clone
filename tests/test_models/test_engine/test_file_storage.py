#!/usr/bin/python3
"""User tests"""


from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import TestBase
import os
import unittest


class Testcity(TestBase):
    """FileStorage tests"""

    def __init__(self, *args, **kwargs):
        """FileStorage tests"""

        super().__init__(*args, **kwargs)
        self._cls = FileStorage
        self._name = 'FileStorage'

    def test_FileStorage(self):
        """FileStorage tests"""
        test_file = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_instance(self):
        """FileStorage tests"""
        my_file_storage = FileStorage()
        self.assertIsInstance(my_file_storage, FileStorage)
