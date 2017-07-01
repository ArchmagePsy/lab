from lab import *
import unittest

class finderTest(unittest.TestCase):
    def test_resource_finder(self):
        resourceTree = Utilities.
        self.assertEqual(resourceTree.resources[1].name, "lab", 'second item in working directory does not have name property "lab"')

if __name__ == '__main__':
    unittest.main()
