from Lab import Utilities
import subprocess, argparse, string

class Task(object):
    __task_func = None

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

    def setup(self, func):
        if callable(func):
            func(self)
        else:
            raise TypeError("Func parameter for setup must be a callable object")

    def __call__(self, project, **kwargs):
        if self.task_function != None:
            return self.task_function(project, **kwargs)
        else:
            raise UndefinedTaskError("this task has not been defined")

class UndefinedTaskError(BaseException):
    pass

class Command(Task):
    __command = str()
    __arg_parser = None

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

    @property
    def parser(self):
        return self.__arg_parser

    def setup_parser(self): # write test for this
        self.__arg_parser = argparse.ArgumentParser()
        for _, name, _, _ in string.Formatter().parse(self.command):
            if name:
                self.parser.add_argument("--" + name, dest = name, required = True)

    def __init__(self, command):
        self.command = command
        @self.define
        def process_command(project, args = None, **kwargs):
            if not kwargs or args != None:
                kwargs = vars(self.parser.parse_known_args(args = args)[0])
            elif kwargs:
                Utilities.mutate_dict(str, kwargs)
            return subprocess.call(self.command.format(**kwargs), shell = True)

class Clean(Command):
    def __init__(self):
        Command.__init__(self, "rm -vf {directory}/*")

class Routine(Task):
    def __call__(self, project):
        if self.task_function != None:
            return self.task_function(project)
        else:
            raise UndefinedTaskError("this task has not been defined")

def add_builtins(project):
    project["_main" : Routine]
    project["clean" : Clean]
