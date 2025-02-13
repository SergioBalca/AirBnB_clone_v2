#!/usr/bin/python3
"""Module with tests for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test for review"""

    def __init__(self, *args, **kwargs):
        """ Test for Review"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test for place id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test for user id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test for text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
