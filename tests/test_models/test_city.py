#!/usr/bin/python3
""" Module with tests for City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test for City"""

    def __init__(self, *args, **kwargs):
        """ Test for City"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test for state_id attribute"""
        new = self.value()
        self.assertEqual(type("new.state_id"), str)

    def test_name(self):
        """ Test for name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
