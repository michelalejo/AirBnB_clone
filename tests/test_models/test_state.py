#!/usr/bin/python3
"""State tests"""

from models.state import State
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestState (TestBase):
    """State tests"""

    def __init__(self, *args, **kwargs):
        """State tests"""
        super().__init__(*args, **kwargs)
        self._cls = State
        self._name = 'State'

    def test_permissions(self):
        """State tests"""
        is_read_true = os.access('models/state.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/state.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/state.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test__instance(self):
        """State tests"""
        my_state = State()
        self.assertIsInstance(my_state, State)
