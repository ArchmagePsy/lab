from lab import *
import unittest

class finderTest(unittest.TestCase):
    def test_resource_finder(self):
        resourceTree = Utilities.findResources()
        # some assert stuff here

if __name__ == '__main__':
    unittest.main()
