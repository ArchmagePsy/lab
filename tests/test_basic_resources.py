from Lab import Resources
import unittest, tempfile

class ResourceTest(unittest.TestCase):
    def test_pretty(self):
        test_ressources = Resources.ResourceList("Parent", [Resources.Resource("Child")])
        self.assertEqual(Resources.pretty(test_ressources), "Parent: ResourceList\n    Child: Resource\n")

    def test_resource(self):
        test_res = Resources.Resource("test")
        self.assertEqual(test_res.name, "test")

    def test_file(self):
        test_file = tempfile.NamedTemporaryFile()
        test_res = Resources.File("test", test_file.name)
        self.assertEqual(test_res.name, "test")
        self.assertEqual(test_res.path, test_file.name)
        test_file.close()

    def test_resource_list(self):
        test_res_list = Resources.ResourceList("test", [
            Resources.Resource("test_0"),
            Resources.Resource("test_1"),
            Resources.Resource("test_2"),
            Resources.Resource("test_3"),
            Resources.Resource("test_4"),
        ])

        self.assertEqual(test_res_list.name, "test")
        for i, r in enumerate(test_res_list.resources):
            self.assertEqual(r.name, "test_" + str(i))

        test_res = Resources.Resource("test_5")
        test_res_list.add(test_res)

        self.assertIn(test_res, test_res_list.resources)

        test_res_list.remove(test_res)

        self.assertNotIn(test_res, test_res_list.resources)

# excluded flder and filelist for now but should add them later
