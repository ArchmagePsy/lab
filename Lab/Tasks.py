import subprocess, argparse, string, Utilities

class Task(object):
    __task_func = None
    __arg_parser = argparse.ArgumentParser()

    @property
    def parser(self):
        return self.__arg_parser

    @property
    def task_function(self):
        return self.__task_func

    @task_function.setter
    def task_function(self, func):
        if callable(func):
            self.__task_func =  func
        else:
            raise TypeError("Task_function must be a callable object")

    def define(self, func):
        self.task_function = func

    def __call__(self, project, args = None, **kwargs):
        if self.task_function:
            if args:
                kwargs.update(Utilities.filter_dict(lambda key, value: bool(value), vars(self.parser.parse_known_args(args = args)[0])))
            return self.task_function(project, **kwargs)
        else:
            raise UndefinedTaskError("this task has not been defined")

class UndefinedTaskError(BaseException):
    pass

class Command(Task):
    __command = str()

    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        if type(value) == str:
            self.__command = value
            self.setup_parser()
        else:
            raise TypeError("Command property must be a string")

    def setup_parser(self): # write test for this
        self._Task__arg_parser = argparse.ArgumentParser()
        for _, name, _, _ in string.Formatter().parse(self.command):
            if name:
                self.parser.add_argument("--" + name, dest = name)

    def __init__(self, command):
        self.command = command
        @self.define
        def process_command(project, **kwargs):
            Utilities.mutate_dict(lambda key, value: str(value), kwargs)
            return subprocess.call(self.command.format(**kwargs), shell = True)

class Clean(Command):
    def __init__(self):
        Command.__init__(self, "rm -vf {directory}/*")

class Routine(Task):
    def __call__(self, project):
        if not self.task_function:
            return self.task_function(project)
        else:
            raise UndefinedTaskError("this task has not been defined")

def add_builtins(project):
    project["clean" : Clean]
