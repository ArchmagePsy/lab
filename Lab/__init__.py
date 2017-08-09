import shutil, argparse, pickle, time, sys
from Lab import Tasks, Utilities

parser = argparse.ArgumentParser()
parser.add_argument("routine", help = "routine(s) to be run", nargs = "*")

class Settings(object):
    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def save(self, directory = shutil.os.getcwd()):
        with open(shutil.os.path.join(directory, "settings"), "wb+") as settings:
            pickle.dump(self, settings)

    @staticmethod
    def load(directory = shutil.os.getcwd()):
        with open(shutil.os.path.join(directory, "settings"), "rb+") as settings:
            return pickle.load(settings)

class lab(object):

    __tasks = dict()
    __settings = None

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

    @classmethod
    def setup(cls):
        def wrapper(func):
            ret = cls()
            func(ret)
        return wrapper

    def __main__(self, args):
        pass

    def __exit__(self):
        pass

    def main(self):
        args = parser.parse_args()
        if args.routine:
            for r in args.routine:
                if isinstance(self.tasks[r], Tasks.Routine):
                    print self(r)
        else:
            self("_main")
        self.__main__(args)
        self.__exit__()

    def __init__(self):
        Tasks.add_builtins(self)

# implement project settings to store runtime etc.
# pickle settings
# figure out syntax for creating named labs
