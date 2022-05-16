#!/usr/bin/python3
""" Module that contains tests for Amenity class """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test for Amenity class that inherits from Basemodel"""

    def __init__(self, *args, **kwargs):
        """Test for Amenities"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test for amenities"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
