"""
Sample tests
"""
from . import calc

from django.test import SimpleTestCase

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together"""
        result = calc.add(5,6)
        self.assertEqual(result, 11)