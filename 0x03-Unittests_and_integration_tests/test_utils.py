#!/usr/bin/env python3
'''a test file for utils.access_nested_map in the utils.py module'''
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    '''a method to test that the method returns what it is supposed to.'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Test method for access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''parameterize a unit test'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''to implement the get__json method to test whether it returns ex res.'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        ''' self descriptive'''
        class Mocked(Mock):
            '''a  mocked class'''

            def json(self):
                ''' json method mocked'''
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''parameterize and patch'''
    def test_memoize(self):
        '''define a class inside test_memoize'''
        class TestClass:
            '''test cases'''
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_md:
            test_instance = TestClass()
            res1 = test_instance.a_property
            res2 = test_instance.a_property

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            mock_md.asset_called_once()
