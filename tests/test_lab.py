from Lab import lab
import unittest, Lab

class LabTest(unittest.TestCase):
    def test_lab(self):
        @lab.setup("test", [])
        def setup(project):
            @project.dummy_task.define
            def dummy_task(project):
                return "I'm kinda dumb aren't I?"

        print Lab.Global.root.test.fetch()[0]("dummy_task")

        self.assertEqual(Lab.Global.test.fetch()[0]("dummy_task"), "I'm kinda dumb aren't I?")
