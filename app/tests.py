from django.test import TestCase
from calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that two nembers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that values are subtracted and returned"""
        self.assertEqual(subtract(11, 5), 6)