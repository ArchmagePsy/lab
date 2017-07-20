from Lab import Utilities, Resources
import subprocess

class Task(object):
    __task_func = None

    @property
    def task_function(self):
        return self.__task_func

    @task_function.setter
    def task_function(self, func):
        self.define(func)

    def define(self, func):
        self.__task_func =  func

    def setup(self, func):
        func(self)

    def __call__(self, project, **kwargs):
        if self.task_function != None:
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

    def __init__(self, command):
        self.command = command
        @self.define
        def process_command(project, **kwargs):
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

class Scan(Routine):
    def __init__(self):
        @self.define
        def scan(project):
            return Resources.pretty(project)

def add_builtins(project):
    project["main" : Routine]
    project["scan" : Scan]
