from lab import Utilities
from lab import Resources
import unittest

class UtilityTest(unittest.TestCase):
    def test_search_until(self):
        self.assertEqual(Utilities.search_until([1, 0], 1), [1])
        self.assertEqual(Utilities.search_until([1, 0], 2), [])

    def test_binary_search(self):
        self.assertEqual(Utilities.binary_search(sorted([1, 0]), 1), [1])
        self.assertEqual(Utilities.binary_search(sorted([1, 1, 0, 1]), 1), [1, 1, 1])
        self.assertEqual(Utilities.binary_search(sorted([1, 0]), 2), [])
