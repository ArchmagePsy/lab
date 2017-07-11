class Task(object):
    __task_func__ = None

    @property
    def task_function(self):
        return self.__task_func__

    @task_function.setter
    def task_function(self, func):
        self.define(func)

    def define(self, func):
        self.__task_func__ =  func

    def __call__(self, project):
        if self.task_function != None:
            return self.task_function(project)
        else:
            raise UndefinedTaskError

class UndefinedTaskError(BaseException):
    message = "undefined task"
