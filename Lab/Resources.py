import shutil

class Resource(object):
    __name = str()

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

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
        if type(value) == str and shutil.os.path.isfile(value):
            self.__path = shutil.os.path.abspath(value) if not shutil.os.path.isabs(value) else value
        else:
            raise TypeError("Path must be a string refrencing a file via standard path syntax")

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
        if type(value) == list and all(map(labda item: isinstance(item, Resource), value)):
            self.__resources = value
        else:
            raise TypeError("Resources must be a list of Resource objects ")

    def add(self, resource):
        if isinstance(resource, Resource):
            self.resources.append(resource)
        else:
            raise TypeError("Cannot append a non-Resource object to resources")

    def remove(self, item):
        if item in self.resources:
            self.resources.pop(self.resources.index(item))
        else:
            raise AttributeError("item could not be found in resources")

    def __getitem__(self, index):
        return self.resources[index]

class FileList(ResourceList):
    def __init__(self, name, files):
        ResourceList.__init__(self, name, files)

    def add(self, resource):
        if isinstance(resource, File):
            self.resources.append(resource)
        else:
            raise TypeError("Cannot append a non-File object to resources")

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
        if type(value) == str and shutil.os.path.isdir(value):
            self.__path = shutil.os.path.abspath(value) if not shutil.os.path.isabs(value) else value
        else:
            raise TypeError("Path must be a string refrencing a folder via standard path syntax")

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
