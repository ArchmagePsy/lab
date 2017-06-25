import subprocess, os, pickle, time

def makeIfNotPresent(filepath):
    dirpath = os.path.dirname(filepath)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

class loadable:

    def __save__(self):
        pass

    def save(self, path):
        path = os.path.abspath(path)
        self.__save__()
        makeIfNotPresent(path)
        with open(os.path.join(path, self.name), "wb+") as fp:
            pickle.dump(self, fp)

    @classmethod
    def load(cls, filepath):
        if os.path.exists(filepath) and os.path.isfile(filepath):
            with open(filepath, "rb") as fp:
                ret = pickle.load(fp)
        else:
            ret = cls()
            ret.name = os.path.basename(filepath)
        return ret

class Recipe(list): # stack to store the apparatus to be run
    pass

class Resource:
    __type = str() # upper string
    __filetype = str() # extension without the .
    __path = str() # absolute path of the resource
    __name = str() # filename
    __modtime = int() # modification time

    def __init_(self, Type, Name):
        self.___type = Type.upper()

    def procName(self, func):
        func(self.path)

    def procFile(self, func):
        with open(self.path, "rb") as fp:
            func(fp)

    def __repr__(self):
        return self.path

    def __str__(self):
        return self.path

    @property
    def name(self):
        return self.__name

    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def Type(self):
        return self.__type

    @Type.setter
    def setType(self, Type):
        self.__type = Type.upper()

    @property
    def filetype(self):
        return self.__filetype

    @filetype.setter
    def setFiletype(self, filetype):
        if "FILE" in self.Type.split(";"):
            self.__filetype = filetype

    @property
    def path(self):
        if "FILE" in self.Type.split(";"):
            return os.path.abspath(self.name + "." + )

class Resources(list):
    def updated(self):# filter all resources by their modification time
        pass

class Target:
    __parent = None # lab
    __aparatus = None # function: def job(parent (lab), resources (array)): success (boolean)
    __resources = Resources() # array of resources

class Record(loadable):

    __timestamp = int()
    __name = str()

    @property
    def name(self):
        return self.__name

    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def timestamp(self):
        return self.__timestamp

    def __save__(self):
        self.stamp()

    def stamp(self):
        self.__timestamp = time.time()

class Config(loadable):

    def __setattribute__(self, name, value):
        setattr(self, name, value)

class lab:
    __record = None
    __config = None

    def __init__(self, **kwargs):
        labFolder = os.path.abspath(".lab")
        print labFolder
        if not os.path.exists(labFolder): os.makedirs(labFolder)
        self.__record = Record.load(labFolder + "/" + kwargs["record_name"])
        self.__config = Config.load(labFolder + "/" + kwargs["config_name"])

    @property
    def record(self):
        return self.__record

    @property
    def config(self):
        return self.__config

    def build(self): # impl Recipe generation
        pass

    def __del__(self):
        self.record.save(".lab/")
        self.config.save(".lab/")

if __name__ == "__main__":
    print "tests to go here"

"""
labs will have a list of targets
each target will have an aparatus

the lab will have a build method that
generates a Recipe from all its targets
the Recipe will contain the instructions
needed to process the aparatus using
only the files that have been modified
by checking the timestamp against that
of the record

write setup.py and turn into
python module
"""
