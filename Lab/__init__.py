import shutil, argparse, sys, shlex, Tasks, Utilities

parser = argparse.ArgumentParser()
parser.add_argument("task", help = "task(s) to be run")

class lab(object):

    __tasks = dict()
    __settings = None

    def __getattr__(self, key):
        return self.tasks[key]

    def __getitem__(self, key):
        if isinstance(key, slice):
            name, task_type, args = key.start, key.stop, key.step
            if issubclass(task_type, Tasks.Task):
                task = task_type() if args == None else task_type(*args)
                self.tasks[name] = task
                return task
            else:
                raise TypeError("Task_type must be a subclass or instance of Task")
        else:
            raise TypeError("Key must be a subclass or instance of slice")

    def __call__(self, query, incremental = True, **kwargs):
        if incremental:
            kwargs.update(runtime = self.settings.runtime)
        return Utilities.select(query, **kwargs)

    @property
    def tasks(self):
        return self.__tasks

    @property
    def settings(self):
        return self.__settings

    def exit(self):
        self.settings.runtime = Utilities.time_stamp()
        self.settings.save()

    def main(self):
        while True:
            user_input = raw_input("> ").strip()
            if user_input.upper() in ["EXIT", "QUIT"]:
                break
            args, leftovers = parser.parse_known_args(args = shlex.split(user_input))
            if args.task:
                if isinstance(self.tasks[args.task], Tasks.Task):
                    self.tasks[args.task](self, args = leftovers)
        self.exit()

    def __init__(self, settings_dir = shutil.os.getcwd()):
        settings_path = shutil.os.path.join(settings_dir, "settings")
        if shutil.os.path.exists(settings_path) and shutil.os.path.isfile(settings_path):
            self.__settings = Utilities.Settings.load(settings_dir)
        else:
            self.__settings = Utilities.Settings(directory = settings_dir)
            self.settings.runtime = 0
        Tasks.add_builtins(self)

# try and configure github pages with jekyll
# or hugo to make a nice project page
# then start C and Scaffolding submodules
