import os

class Resource(object):
    __name = str()

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

class File(Resource):
    __path = str()

    def __init__(self, name, path):
        self.name = name
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = os.path.abspath(value)

class ResourceList(Resource):
    __resources = list()

    def __init__(self, name, resources):
        Resource.__init__(self, name)
        self.resources = resources

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        self.__resources = value

    def add(self, resource):
        if isinstance(resource, Resource): self.resources.append(resource)

    def remove(self, item):
        if item in self.resources: self.resources.pop(self.resources.index(item))

class FileList(ResourceList):
    def __init__(self, name, files):
        ResourceList.__init__(self, name, files)

class Folder(FileList):
    __path = str()

    def __init__(self, name, files, path):
        FileList.__init__(self, name, files)
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = os.path.abspath(value)

    def add(self, resource):
        if isinstance(resource, File): self.resources.append(resource)

def pretty(base, indent = 4, level = 0):
    if isinstance(base, ResourceList):
        ret = (" " * (indent * level)) + base.name + ": " + base.__class__.__name__ + "\n"
        for r in base.resources:
            ret += pretty(r, level = level + 1)
        return ret
    elif isinstance(base, Resource):
        return (" " * (indent * level)) + base.name + ": " + base.__class__.__name__ + "\n"

"""
add more resource types such as artifacts, objects, libraries
and seperate them by language e.g a c submodule for c based
resources
"""
