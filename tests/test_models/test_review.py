#!/usr/bin/python3
"""Review tests"""


from models.review import Review
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestReview (TestBase):
    """Review tests"""

    def __init__(self, *args, **kwargs):
        """Review tests"""

        super().__init__(*args, **kwargs)
        self._cls = Review
        self._name = 'Review'

    def test_permissions(self):
        """Review tests"""
        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """Review tests"""
        my_review = Review()
        self.assertIsInstance(my_review, Review)
