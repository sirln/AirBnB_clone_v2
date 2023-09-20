#!/usr/bin/python3
"""
City class unittest module
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Unit tests for the `City` class model.
    """

    def __init__(self, *args, **kwargs):
        """
        Testing initialization of City model with kwargs
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

'''    def test_state_id(self):
        """
        Test if `state_id` attribute of the `City` model
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test if `name` attribute of the `City` model
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)'''
