#!/usr/bin/python3
"""User tests"""


from models.state import State
from tests.test_models.test_base_model import TestBasa
import os
import unittest

class TestState (TestBase):
    """User tests"""

    def __init__(self, *args, **kwargs):
        """User tests"""
        super().__init__(*args, **kwargs)
        self._cls = State
        self._name = 'State'

    def test_permissions(self):
        """User tests"""
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """User tests"""
        my_user = State()
        self.assertIsInstance(my_state, State)
