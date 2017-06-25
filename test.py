from lab import *

with lab("test_project") as proj:
    with proj.tasks.test as test:
        @test.check
        def check(self):
            return True

        @test.execute
        def execute(self):
            compile(self.proj.select.type("source").all().fetch())
