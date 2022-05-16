#!/usr/bin/python3
"""Module with tests for State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ tests for state"""

    def __init__(self, *args, **kwargs):
        """ tests for state"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test for state"""
        new = self.value()
        self.assertEqual(type(new.name), str)
