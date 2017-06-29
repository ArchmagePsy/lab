from lab import Resources
from lab import Utilities

Global = Resources.ResourceList("global", [])
GlobalSelector = Utilities.Selector(Global)

class lab(ResourceList):

    @property
    def select(self):
        return Utilities.Selector(self)

    def __init__(self, name, setup):
        global Global
        Resources.ResourceList.__init__(self, name)
        Global.add(self)
        setup(self)

"""
use binary search in getattribute to
search for everything that matches by name
"""
