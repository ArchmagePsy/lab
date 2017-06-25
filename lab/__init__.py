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

    def __getattribute__(self, name):
        pass
"""
use binary search in getattribute to
search for everything that matches by name
"""
