from Lab import lab, Tasks, Settings
import unittest, tempfile, shutil

class LabTest(unittest.TestCase):
    def test_lab(self):
        @lab.setup()
        def setup(project):
            project["dummy_task" : Tasks.Task]
            @project.dummy_task.define
            def dummy_task(project):
                return "I'm kinda dumb aren't I?"

    def test_lab_2(self):
        @lab.setup()
        def setup(project):
            project["dummy_command" : Tasks.Command : ["echo hello world"]]

    def test_settings(self):
        settings = Settings()
        settings.foo = "bar"
        self.assertEqual(settings.foo, "bar")

    def test_settings_load_and_save(self):
        settings = Settings()
        settings.foo = "bar"
        dir_path = tempfile.mkdtemp()
        settings.save(directory = dir_path)
        self.assertEqual(Settings.load(directory = dir_path).foo, "bar")
        shutil.rmtree(dir_path)
