"""Tests for text slugification, runnable with pytest or unittest."""

import unittest

from slugify import slugify


class SlugifyTests(unittest.TestCase):
    def test_required_examples(self):
        cases = [
            (" Hello World! ", "hello-world"),
            ("foo--bar", "foo-bar"),
            ("___leading", "leading"),
            ("trailing___", "trailing"),
            ("UPPER", "upper"),
            ("a!@#b", "a-b"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_empty_and_separator_only_inputs(self):
        for text in ("", " ", "\t\n\r", "!@#", "___", "---", " _!-\t "):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), "")

    def test_alphanumeric_boundaries(self):
        for text, expected in (("A", "a"), ("7", "7"), ("AbC123", "abc123")):
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_mixed_separator_runs(self):
        self.assertEqual(slugify("__Foo \t\n--!Bar...Baz__"), "foo-bar-baz")

    def test_existing_slug_is_preserved(self):
        self.assertEqual(slugify("hello-world-123"), "hello-world-123")

    def test_unicode_alphanumeric_characters_are_preserved(self):
        self.assertEqual(slugify(" CAFÉ 世界 ١٢ "), "café-世界-١٢")
