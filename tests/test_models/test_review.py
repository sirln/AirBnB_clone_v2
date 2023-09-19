#!/usr/bin/python3
"""
Unittest module for the Review class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Unit tests for the Review class. """

    def __init__(self, *args, **kwargs):
        """ Test for initialization """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test if 'place_id' attribute of the Review
        class is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test if 'user_id' attribute of the Review
        class is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test if 'text' attribute of the Review
        class is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
