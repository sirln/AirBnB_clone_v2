#!/usr/bin/python3
"""
Unittest module for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class TestReview(unittest.TestCase):
    """ Unit tests for the Review class. """
    def setUp(self):
        """Set up test instance and attributes."""
        self.review = Review()

    def tearDown(self):
        """Tear down test instance."""
        del self.review

    def test_instance_inheritance(self):
        """Test Review inherits from BaseModel and Base."""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(Review, Base))

    def test_tablename(self):
        """Test correct tablename."""
        self.assertEqual(self.review.__tablename__, "reviews")


if __name__ == "__main__":
    unittest.main()
