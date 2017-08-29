from Lab import Tasks, Utilities
import unittest, tempfile, shutil, shlex, argparse

class TaskTest(unittest.TestCase):
    def test_task(self):
        dummy_task = Tasks.Task()
        @dummy_task.define
        def dummy(project):
            return "I'm just a dummy"
        self.assertEqual(dummy_task(None), "I'm just a dummy")

    def test_task_undefined(self):
        dummy_task = Tasks.Task()
        with self.assertRaises(Tasks.UndefinedTaskError) as SE:
            dummy_task(None)

    def test_clean_task(self):
        dir_path = tempfile.mkdtemp()
        files = []
        for i in range(3):
            with open(shutil.os.path.join(dir_path, str(i)), "w+") as fp:
                files.append(fp.name)
        clean = Tasks.Clean()
        clean(None, args = shlex.split("--directory " + dir_path))
        self.assertTrue(all([not shutil.os.path.exists(f) for f in files]))
        shutil.os.rmdir(dir_path)

    def test_setup_parser(self):
        test = Tasks.Command("echo 'testing {file}'")
        self.assertEqual(test.parser._actions[1].option_strings, ["--file"])
