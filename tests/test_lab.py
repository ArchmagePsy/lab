from Lab import lab, Global, Tasks
import unittest

class LabTest(unittest.TestCase):
    def test_lab(self):
        @lab.setup("test")
        def setup(project):
            project["dummy_task" : Tasks.Task]
            @project.dummy_task.define
            def dummy_task(project):
                return "I'm kinda dumb aren't I?"

        self.assertEqual(Global.root.test.fetch()[0]("dummy_task"), "I'm kinda dumb aren't I?")

    def test_lab_2(self):
        @lab.setup("test2")
        def setup(project):
            project["dummy_command" : Tasks.Command : ["echo hello world"]]

        self.assertEqual(Global.root.test.fetch()[0]("dummy_command"), 0)
