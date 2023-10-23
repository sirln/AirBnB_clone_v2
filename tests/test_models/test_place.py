#!/usr/bin/python3
"""
Unittest module for the Place class.
"""
import unittest
from models.place import Place
from models.amenity import Amenity
from sqlalchemy.exc import IntegrityError
from os import getenv, environ


class TestPlace(unittest.TestCase):
    """Defines tests for the Place class."""
    def setUp(self):
        """Setup for each test method"""
        self.place = Place(
                            city_id="1234abcd",
                            user_id="abcd1234",
                            name="Test Place",
                            description="A test place in a test city"
                           )

    def tearDown(self):
        """Teardown after each test method"""
        del self.place

    def test_attributes(self):
        """Test the attributes and default values of Place"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))

        # self.assertEqual(self.place.number_rooms, 0)
        # self.assertEqual(self.place.number_bathrooms, 0)
        # self.assertEqual(self.place.max_guest, 0)
        # self.assertEqual(self.place.price_by_night, 0)

    def test_db_storage_amenities(self):
        """Test amenities attribute behavior for DBStorage"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertTrue(hasattr(self.place, "amenities"))
            self.assertIsInstance(self.place.amenities, list)


if __name__ == "__main__":
    unittest.main()
