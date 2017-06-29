from lab import Resources
import os

def search_until(array, target, key = lambda item: item):
    results = []
    for item in array:
        if key(item) == target:
            results.append(item)
        else:
            break
    return results

def binary_search(array, target, key = lambda item: item):
    results = []
    tmpArray = array
    searching = True
    while searching:
        index = len(tmpArray) // 2
        current = tmpArray[index]
        if key(current) == target:
            results += search_until(reversed(tmpArray[:index]), target)
            results.append(current)
            results += search_until(tmpArray[index + 1:], target)
            searching = False
        elif key(current) > target:
            tmpArray = tmpArray[:index]
        elif key(current) < target:
            tmpArray = tmpArray[index + 1:]
    return results

def setEnv(self, name, value):
    os.environ[name] = str(value)

def getEnv(self, name):
    return os.environ[name]


def clean(directory):
    pass

def sortBy(array, by):
    return sorted(array, key = lambda item: getattr(item, by) if hasattr(item, by) else "") if by != None else sorted(array)

class Selector:
    __origin = None
    __result = None

    def __init__(self, base):
        if isinstance(base, Resources.ResourceList):
            self.result = base.resources
            self.__origin = base.resources
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
        self.result = sortBy(self.result, "name")
        self.result = binary_search(self.result, name, key = lambda item: item.name)
        return self

    def fetch(self):
        ret = self.result
        self.result = self.origin
        return ret
