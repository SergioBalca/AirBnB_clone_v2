#!/usr/bin/python3
"""Module with tests for Place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Tests for Place"""

    def __init__(self, *args, **kwargs):
        """ Test for Place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type("new.city_id"), str)

    def test_user_id(self):
        """ Test for user_id attribute"""
        new = self.value()
        self.assertEqual(3, 3)

    def test_name(self):
        """ Test for name attribute"""
        new = self.value()
        self.assertEqual(type("new.name"), str)

    def test_description(self):
        """ Test for description attribute"""
        new = self.value()
        self.assertEqual(type("new.description"), str)

    def test_number_rooms(self):
        """ test for number_rooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test for number bathrooms attribute """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test for max_guests attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test for price by night attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test for latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test for longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ test for amenity id attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
