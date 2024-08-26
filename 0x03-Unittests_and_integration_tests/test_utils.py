#!/usr/bin/env python3
""" Testing access_nested_map """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


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
