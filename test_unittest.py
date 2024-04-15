import unittest

from main import make_upper_case, make_lower_case

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(make_upper_case("foo"), 'FOO')

    def test_lower(self):
        self.assertEqual(make_lower_case("HOLA"), "hola")
    