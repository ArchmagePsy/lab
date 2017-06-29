from lab import *

@lab.setup("test_project", [Resources.Resource("dummy")])
def setup(proj):
    print proj.select.dummy.fetch()[0].name
    print proj.select.idontexist.fetch()
