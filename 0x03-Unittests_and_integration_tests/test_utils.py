#!/usr/bin/env python3
"""This is the utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """This class inherits from unittest.TestCase"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """
        This method tests the access_nested_map function with various
        inputs and checks if the output matches the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """
        This method tests the get_json function with
        mocked HTTP responses using unittest.mock.patch
        It checks if the returned JSON matches the expected payload and if the
        requests.get function is called with the correct URL.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This method tests the memoization behavior by creating
    a class TestClass with a method a_method and a memoized
    property a_property
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """
        This method tests the get_json function with mocked HTTP
        responses using unittest.mock.patch.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """This class inherits from unittest.TestCase."""

    def test_memoize(self) -> None:
        """
        This method tests the memoization behavior by creating a class
        TestClass with a method a_method and a memoized property a_>
        """

        class TestClass:
            """class test class"""

            def a_method(self) -> int:
                """method function"""
                return 42

            @memoize
            def a_property(self) -> int:
                """property function"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
