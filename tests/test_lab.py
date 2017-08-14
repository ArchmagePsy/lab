from Lab import lab, Tasks
import unittest, tempfile, shutil

class LabTest(unittest.TestCase):
    def test_lab(self):# these need fixing
        dir_path = tempfile.mkdtemp()
        @lab.setup(settings_dir = dir_path)
        def setup(project):
            project["dummy_task" : Tasks.Task]
            @project.dummy_task.define
            def dummy_task(project):
                return "I'm kinda dumb aren't I?"
        shutil.rmtree(dir_path)

    def test_lab_2(self):# these need fixing
        dir_path = tempfile.mkdtemp()
        @lab.setup(settings_dir = dir_path)
        def setup(project):
            project["dummy_command" : Tasks.Command : ["echo hello world"]]
        shutil.rmtree(dir_path)

    def test_lab_settings(self):
        dir_path = tempfile.mkdtemp()
        test_project = lab(settings_dir = dir_path)
        test_project.settings.foo = "bar"
        test_project.exit()
        test_project = lab(settings_dir = dir_path)
        self.assertEqual(test_project.settings.foo, "bar")
        shutil.rmtree(dir_path)
