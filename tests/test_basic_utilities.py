from Lab import Utilities, Resources
import tempfile, shutil, unittest

class Dummy:
    foo = int()
    def __init__(self, value):
        self.foo = value

class UtilityTest(unittest.TestCase):
    def test_search_until(self):
        self.assertEqual(Utilities.search_until([1, 0], 1), [1])
        self.assertEqual(Utilities.search_until([1, 0], 2), [])
        self.assertEqual(Utilities.search_until([(0, 1), (1, 0), (2, 1)], 0, key = lambda item: item[0]), [(0, 1)])
        self.assertEqual(Utilities.search_until([(0, 1), (1, 0), (2, 1)], 1, key = lambda item: item[0]), [])

    def test_binary_search(self):
        self.assertEqual(Utilities.binary_search(sorted([1, 0]), 1), [1])
        self.assertEqual(Utilities.binary_search(sorted([1, 1, 0, 1]), 1), [1, 1, 1])
        self.assertEqual(Utilities.binary_search(sorted([1, 0]), 2), [])

    def test_env(self):
        Utilities.set_env("dummy", 1)
        self.assertEqual("1", Utilities.get_env("dummy"))

    def test_sort_by(self):
        self.assertEqual(Utilities.sort_by([9, 5, 9, 4, 5, 1, 9, 5, 6, 1, 0, 6, 1, 0, 6]), [0, 0, 1, 1, 1, 4, 5, 5, 5, 6, 6, 6, 9, 9, 9])
        tmp_array = [Dummy(1), Dummy(4), Dummy(3)]
        self.assertEqual(Utilities.sort_by(tmp_array, by = "foo" ), sorted(tmp_array, key = lambda item: item.foo))

    def test_find_resources(self):
        dir_path = tempfile.mkdtemp()
        temporary_file = tempfile.NamedTemporaryFile(dir = dir_path)

        self.assertEqual(Resources.pretty(Utilities.find_resources(root = dir_path)), "%s: Folder\n    %s: File\n" % (shutil.os.path.basename(dir_path), shutil.os.path.basename(temporary_file.name)))

        temporary_file.close()
        shutil.rmtree(dir_path)

    def test_mutate_dict(self):
        self.assertEqual(Utilities.mutate_dict(lambda item: item + 1, {"foo": 1, "bar": 1}), {"foo": 2, "bar": 2})