from lab import Resources
import os

def search_until(array, target):
    results = []
    for item in array[index + 1:]:
        if key(item) == target:
            results.append(item)
        else:
            break
    return results

def binary_search(array, target, key = lambda item: item):
    results = []
    tmpArray = array
    while True:
        index = len(tmpArray // 2)
        current = key(tmpArray[index])
        if current == target:
            results += search_until(reversed(tmpArray[:index]))
            results.append(current)
            results += search_until(tmpArray[index + 1:])
        elif current > target:
            tmpArray = tmpArray[:index]
        elif current < target:
            tmpArray = tmpArray[index + 1:]
    return results

def setEnv(self, name, value):
    os.environ[name] = str(value)

def getEnv(self, name):
    return os.environ[name]


def clean(directory):
    pass

class Selector:
    __origin = None
    __result = None

    def __init__(self, base):
        if isinstance(base, Resources.Resource):
            self.result = base
            self.__origin = base
        else:
            raise TypeError("base must be a subclass or instance of Resources.Resource")

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        if isinstance(value, Resources.Resource):
            self.__result = value
        elif type(value) == list:
            self.__result.resources = value

    @property
    def origin(self):
        return self.__origin

    def __getattr__(self, name):
        print name
        if isinstance(self.result, Resources.ResourceList):
            self.result = self.result.sort(by = "name")
            self.result = binary_search(self.result.resources, name, key = lambda item: item.name)
        return self

    def fetch(self):
        ret = self.result
        self.result = self.origin
        return ret
