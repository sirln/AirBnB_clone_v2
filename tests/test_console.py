#!/usr/bin/python3
'''
Console unittest module
'''
import os
import sys
import unittest
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    '''
    Defining the console test cases
    '''

    def setUp(self):
        """Set up testing environment"""
        try:
            os.rename("siso.json", "tmp")
        except IOError:
            pass

        self.hbnb_cmd = HBNBCommand()

    def test_create_no_class(self):
        """Test 'create' with no class argument"""
        backup = sys.stdout
        sys.stdout = StringIO()
        self.hbnb_cmd.onecmd("create")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")
        sys.stdout = backup

    def test_create_invalid_class(self):
        """Test 'create' with invalid class argument"""
        backup = sys.stdout
        sys.stdout = StringIO()
        self.hbnb_cmd.onecmd("create InvalidClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")
        sys.stdout = backup

    def test_create_string_param(self):
        """Test 'create' with string parameters"""
        self.hbnb_cmd.onecmd('create User name="John_Doe"')

    def test_create_float_param(self):
        """Test 'create' with float parameters"""
        self.hbnb_cmd.onecmd('create Place latitude=3.14')

    def test_create_int_param(self):
        """Test 'create' with integer parameters"""
        self.hbnb_cmd.onecmd('create State population=5000')

    def test_create_mixed_params(self):
        """Test 'create' with mixed parameters"""
        args = f'create City name="Sunny_City" population=400000 latitude=4.44'
        self.hbnb_cmd.onecmd(args)

    def test_create_invalid_params(self):
        """Test 'create' with invalid parameters"""
        self.hbnb_cmd.onecmd('create User "John_Doe"')


if __name__ == "__main__":
    unittest.main()
