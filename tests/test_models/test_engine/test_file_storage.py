#!/usr/bin/python3
"""User tests"""


from models.file_storage import City
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
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """FileStorage tests"""
        my_file_storage = FileStorage()
        self.assertIsInstance(my_file_storage, FileStorage)
