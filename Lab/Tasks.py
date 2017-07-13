from Lab import Utilities
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

    def __call__(self, project, *args, **kwargs):
        if self.task_function != None:
            return self.task_function(project, *args, **kwargs)
        else:
            raise UndefinedTaskError

class UndefinedTaskError(BaseException):
    message = "undefined task"

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
        def process_command(project, *args, **kwargs):
            Utilities.mutate_dict(str, kwargs)
            return subprocess.call(self.command.format(**kwargs), shell = True)

class Clean(Command):
    def __init__(self):
        Command.__init__(self, "rm -vf {directory}/*")
