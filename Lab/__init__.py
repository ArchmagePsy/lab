import shutil, argparse
from Lab import Resources, Utilities, Tasks

Global_resources = Resources.ResourceList("labs", [])
Global = Utilities.Selector(Global_resources)

parser = argparse.ArgumentParser()
parser.add_argument("routine", help = "routine(s) to be run", nargs = "*")

class lab(Resources.ResourceList):

    __tasks = dict()

    def __getattr__(self, key):
        return self.tasks[key]

    def __getitem__(self, key):
        if isinstance(key, slice):
            name, task_type, args = key.start, key.stop, key.step
            if not self.tasks.has_key(name) and issubclass(task_type, Tasks.Task):
                task = task_type() if args == None else task_type(*args)
                self.tasks[name] = task
                return task

    def __call__(self, task_name, **kwargs):
        if self.tasks.has_key(task_name):
            return self.tasks[task_name](self, **kwargs)

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

    def __main__(self, args):
        pass

    def main(self):
        global parser
        args = parser.parse_args()
        if args.routine:
            for r in args.routine:
                if isinstance(self.tasks[r], Tasks.Routine):
                    print self(r)
        else:
            self("main")
        self.__main__(args)

    def __init__(self, name, base = []):
        global Global_resources
        if shutil.os.path.basename(shutil.os.getcwd()):
            base = Utilities.find_resources()
        Resources.ResourceList.__init__(self, name, base)
        Tasks.add_builtins(self)
        Global_resources.add(self)
