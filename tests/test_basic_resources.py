from lab import Resources
import unittest

class ResourceTest(unittest.TestCase):
    def test_pretty(self):
        test_ressources = Resources.ResourceList("Parent", [Resources.Resource("Child")])
        self.assertEqual(Resources.pretty(test_ressources), "Parent: ResourceList\n    Child: Resource\n")
