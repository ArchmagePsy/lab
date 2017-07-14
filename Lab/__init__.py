import shutil
from Lab import Resources, Utilities, Tasks

Global_resources = Resources.ResourceList("root", [])
Global = Utilities.Selector(Global_resources)

class lab(Resources.ResourceList):

    __tasks = dict()

    def __getattr__(self, key):
        return self.tasks[key]

    def __getitem__(self, key):
        if isinstance(key, slice):
            name, task_type = key.start, key.stop
            print issubclass(task_type, Tasks.Task)
            if not self.tasks.has_key(name) and issubclass(task_type, Tasks.Task):
                task = task_type()
                self.tasks[name] = task
                return task

    def __call__(self, task_name, *args, **kwargs):
        if self.tasks.has_key(task_name):
            return self.tasks[task_name](self, *args, **kwargs)

    @property
    def tasks(self):
        return self.__tasks

    @property
    def select(self):
        return Utilities.Selector(self)

    @staticmethod
    def setup(name, base = []):
        def wrapper(func):
            ret = lab(name, base = base)
            func(ret)
            return ret
        return wrapper

    def __init__(self, name, base = []):
        global Global_resources
        Resources.ResourceList.__init__(self, name, base)
        Global_resources.add(self)
