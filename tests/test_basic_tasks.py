from lab import Tasks
import unittest

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
