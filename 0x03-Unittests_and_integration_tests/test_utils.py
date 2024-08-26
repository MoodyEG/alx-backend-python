#!/usr/bin/env python3
""" Testing access_nested_map """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
import unittest.mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping[str, Any],
        path: Sequence[str], expected: Any
    ) -> None:
        """ Test access_nested_map function, normally """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        (dict(), ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping[str, Any],
        path: Sequence[str], expected_msg: str
    ) -> None:
        """ Test access_nested_map function, with raise """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """ Test the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, bool],
        mock_get: unittest.mock.Mock
    ) -> None:
        """ Test the get_json function """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test the memoize decorator """
    class TestClass:
        """ Inner class for testing memoize decorator """
        def a_method(self):
            """ Method to be mocked """
            return 42

        @memoize
        def a_property(self):
            """ Property to be tested """
            return self.a_method()

    @unittest.mock.patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method: unittest.mock.Mock) -> None:
        """ Test the memoize decorator """
        test_class = TestMemoize.TestClass()
        test_class.a_property()
        test_class.a_property()
        mock_a_method.assert_called_once()
