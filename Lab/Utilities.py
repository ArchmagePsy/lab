import shutil, time, pickle
"""
This module just contains handy functions that fit into a miscellaneous (?)
category. They're mostly utilized for selection but any algorithms that other parts
of the module need to use will be put here as well.
"""
def search_until(array, target, key = lambda item: item):
    """
    This funtion simply finds all the occurences of target.
    Its only use case is to get the remaining items from the binary search.

    :array: List
    :target: Any
    :key: Callable
    :return: List
    """
    results = []
    for item in array:
        if key(item) == target:
            results.append(item)
        else:
            break
    return results

def binary_search(array, target, key = lambda item: item):
    """
    This is the search function used for selection.
    Its pretty fast and whether or not its the best implementation
    is a tale only time can tell (is that the right phrase?).

    :array: List
    :target: any
    :key: Callable
    :return: List
    """
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

def set_env(name, value):
    """
    Not really sure why or when I'll need this but whatever.
    All it does is set an environment variable.

    :name: String
    :value: Any
    :return: None
    """
    shutil.os.environ[name] = str(value)

def get_env(name):
    """
    I might use these in the future so I'll keep them
    but just in case you couldn't guess this gets an environment variable.

    :name: String
    :return: String
    """
    return str(shutil.os.environ[name])

def sort_by(array, by = None):
    """
    Literally just sorts an array with an optional
    by parameter for lists of objects with members.

    :array: List
    :by: String
    :return: List
    """
    return sorted(array, key = lambda item: getattr(item, by) if hasattr(item, by) else None) if by != None else sorted(array)

def mutate_dict(func, dictionary):# yeah I stole this, thx gens and Ned Batchelder from SO
    """
    A map function for MAPPINGS would be kinda useful but for now this is a good
    implementation from Stack Overflow. Couldn't really make a better one so I just
    did a bit of copypasta. hmmmmm delicous.

    :func: Callable
    :dictionary: Dictionary
    :return: Dictionary
    """
    for key, value in dictionary.iteritems():
        dictionary[key] = func(value)
    return dictionary

class Settings(object):
    """
    Really simple class that is just used to store all the persistent
    information that the lab needs. Uses pickle for serialization just because.
    """
    def __init__(self, directory = shutil.os.getcwd()):
        """
        Just initializes the Settings and sets the directory property up so that
        it can save without having to pass the location every time.

        :directory: String
        :return: Settings
        """
        self.directory = directory

    def __setattr__(self, name, value):
        """
        Syntax sugar for setting members. No more no less.

        :name: String
        :value: Any
        :return: None
        """
        self.__dict__[name] = value

    def save(self):
        """
        Saves the settings to the directory passed in the initializer using pickle

        :return: None
        """
        with open(shutil.os.path.join(self.directory, "settings"), "wb+") as settings:
            pickle.dump(self, settings)

    @staticmethod
    def load(directory):
        """
        Nice method to load the Settings object. Again with pickle.

        :directory: String
        :return: Settings
        """
        with open(shutil.os.path.join(directory, "settings"), "rb+") as settings:
            return pickle.load(settings)

def time_stamp():
    """
    Gets current time. Just a wrapper for time.time().

    :return: Integer
    """
    return int(time.time())

by_name = lambda item: shutil.os.path.splitext(shutil.os.path.basename(item))[0]

def select(query, root = shutil.os.getcwd(), key = by_name, runtime = None):
    """
    This is the function used to get the paths of files in the project.
    Lets the user customize its behaviour and has the option to filter
    out files that haven't been updated since a particular time.

    :query: String (could be Any)
    :root: String
    :key: Callable
    :runtime: Integer
    :return: List
    """
    results = []
    for dirpath, dirs, files in shutil.os.walk(root):
        results.extend(map(lambda item: shutil.os.path.join(dirpath, item), binary_search(sorted(files + dirs), query, key = key)))
    if runtime != None: # test this somehow
        return filter(lambda item: shutil.os.path.getmtime(item) > runtime, results)
    return results
