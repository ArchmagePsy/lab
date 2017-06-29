from lab import Resources
from lab import Utilities

Global = Resources.ResourceList("global", [])
GlobalSelector = Utilities.Selector(Global)

class lab(Resources.ResourceList):

    @property
    def select(self):
        return Utilities.Selector(self)

    @staticmethod
    def setup(name, base, func):
        ret = lab(name, base)
        func(ret)
        return ret

    def __init__(self, name, base):
        global Global
        Resources.ResourceList.__init__(self, name, base)
        Global.add(self)

"""
use binary search in getattribute to
search for everything that matches by name
"""
