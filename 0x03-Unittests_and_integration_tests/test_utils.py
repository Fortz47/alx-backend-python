#!/usr/bin/env python3
"""Module to parameterize unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import Mock, patch
import requests


map1 = {"a": 1}
path1 = ("a",)
res1 = 1  # expected result for map1 and path 1

map2 = {"a": {"b": 2}}  # nested map
path2 = ("a",)
res2 = {'b': 2}

map3 = {"a": {"b": 2}}  # nested map
path3 = ("a", "b")
res3 = 2

paramList = [(map1, path1, res1), (map2, path2, res2), (map3, path3, res3)]


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""
    @parameterized.expand(paramList)
    def test_access_nested_map(self, _map: Mapping, path: Sequence, res: Any) -> None:
        """tests access_nested_map method"""
        self.assertEqual(access_nested_map(_map, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, _map: Mapping, path: Sequence) -> None:
        """Parameterize a unit test"""
        with self.assertRaises(KeyError):
            access_nested_map(_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """test http calls"""
        with patch('requests.get') as mock_req:
            result = get_json(test_url)
            result.return_value = test_payload

            self.assertEqual(result(), test_payload)
            mock_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""
    def test_memoize(self) -> None:
        """test utils.memoize method"""
        class TestClass:
            """Test class"""

            def a_method(self) -> int:
                """a method"""
                return 42

            @memoize
            def a_property(self) -> int:
                """a memoized method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            obj = TestClass()
            obj.a_property()
            obj.a_property()

            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
