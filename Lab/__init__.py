import shutil, argparse, sys
from Lab import Tasks, Utilities

parser = argparse.ArgumentParser()
parser.add_argument("routine", help = "routine(s) to be run")

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

    def __call__(self, query, **kwargs):
        kwargs.update(runtime = self.settings.runtime)
        return Utilities.select(query, **kwargs)

    @property
    def tasks(self):
        return self.__tasks

    @property
    def settings(self):
        return self.__settings

    def setup(self):
        def wrapper(func):
            func(self)
        return wrapper

    def __main__(self, args):
        pass

    def __exit__(self):
        pass

    def exit(self):
        self.__exit__()
        self.settings.runtime = Utilities.time_stamp()
        self.settings.save()

    def main(self, args = None):
        args = parser.parse_known_args(args = args)[0]
        if args.routine:
            if isinstance(self.tasks[args.routine], Tasks.Routine):
                print self(args.routine)
        else:
            self("_main")
        self.__main__(args)
        self.exit()

    def __init__(self, settings_dir = shutil.os.getcwd()):
        settings_path = shutil.os.path.join(settings_dir, "settings")
        if shutil.os.path.exists(settings_path) and shutil.os.path.isfile(settings_path):
            self.__settings = Utilities.Settings.load(settings_dir)
        else:
            self.__settings = Utilities.Settings(directory = settings_dir)
            self.settings.runtime = 0
        Tasks.add_builtins(self)
