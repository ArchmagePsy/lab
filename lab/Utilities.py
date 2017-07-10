import os
from lab import Resources

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
    searching = True
    minimum = 0
    maximum = len(array) - 1
    while True:
        if minimum > maximum:
            break
        mean = (minimum + maximum) // 2
        current = key(array[mean])
        if current == target:
            results += search_until(reversed(array[:mean]), target)
            results.append(array[mean])
            results += search_until(array[mean + 1:], target)
            break
        elif current < target:
            minimum = mean + 1
        elif current > target:
            maximum = mean - 1
    return results

def setEnv(self, name, value):
    os.environ[name] = str(value)

def getEnv(self, name):
    return os.environ[name]


def clean(directory):
    pass

def sortBy(array, by = None):
    return sorted(array, key = lambda item: getattr(item, by) if hasattr(item, by) else None) if by != None else sorted(array)

def findResources(root = os.getcwd()):
    if os.path.isdir(root):
        return Resources.Folder(os.path.basename(root), [findResources(root = os.path.join(root, i)) for i in os.listdir(root)], root)
    elif os.path.isfile(root):
        return Resources.File(os.path.basename(root), root)

class Selector:
    __origin = None
    __result = Resources.ResourceList("results", [])

    def __init__(self, base):
        if isinstance(base, Resources.ResourceList):
            self.result.resources = base.resources
            self.__origin = base.resources
        else:
            raise TypeError("base must be a subclass or instance of Resources.ResourceList")

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
        self.result.resources = sortBy(self.result.resources, "name")
        self.result.resources = binary_search(self.result.resources, name, key = lambda item: item.name)
        return self

    def fetch(self):
        ret = self.result
        self.result = self.origin
        return ret
