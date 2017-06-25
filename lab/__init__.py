import os
from lab import Resources
from lab import Utilities
from lab import Selector

Global = ResourceList("global", [])

class lab(ResourceList):

    @property
    def select(self):
        return selector(self)

    def __init__(self, name):
        ResourceList.__init__(self, name)

"""
use binary search in getattribute to
search for everything that matches by name
"""
