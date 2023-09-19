#!/usr/bin/python3
"""
This module contains the unit tests for the Amenity class
which derives from BaseModel.
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Unit test cases for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test_Amenity instance by setting
        the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test to ensure that the 'name' attribute of the Amenity
        instance is of type 'str'.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
