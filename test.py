from lab import *

@lab.setup("test_project", [Resources.Resource("dummy")])
def setup(proj):
    print self.proj.select.dummy.fetch()[0].name
