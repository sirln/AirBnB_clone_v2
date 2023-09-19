#!/usr/bin/python3
"""
Unittest module for the Place class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Defines tests for the Place class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes for the test class
         """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Tests if 'city_id' attribute is a string.
         """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Tests if 'user_id' attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Tests if 'name' attribute is a string. """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Tests if 'description' attribute is a string. """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Tests if 'number_rooms' attribute is an integer. """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Tests if 'number_bathrooms' attribute is an integer. """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Tests if 'max_guest' attribute is an integer. """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Tests if 'price_by_night' attribute is an integer. """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Tests if 'latitude' attribute is a float. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Tests if 'longitude' attribute is a float. """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Tests if 'amenity_ids' attribute is a list. """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
