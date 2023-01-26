"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)


'''We can use Mock testing to test functions depending on
some external services like requesting data from external APIs
steps are as follows:
    -import APIClient
    -Create client
    -make request
    -check results
    For reference see Mock-test-sample.png'''
