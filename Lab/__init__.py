import shutil, argparse, sys, Tasks, Utilities
"""
This is the starting point for the Lab module where the lab class is defined.
If you were wondering why its called a lab and not a project or build script
the you were wondering pointlessly 'cause its just a classic example of simple
and obnoxious names for tech. also lab is shorter so . . . yeah.
"""

parser = argparse.ArgumentParser()
parser.add_argument("routine", help = "routine(s) to be run")

class lab(object):
    """
    This is the lab and its only purpose is pretty much a glorified container
    for the tasks. It automates some stuff and keeps track of stuff with a
    Settings object.
    """
    __tasks = dict()
    __settings = None

    def __getattr__(self, key):
        """
        Here is some of the sugary goodness that the lab offers.
        this is just fetches your tasks in a nice way using the dot syntax
        that we all love.

        :key: String
        :return: Task
        """
        return self.tasks[key]

    def __getitem__(self, key):
        """
        By overriding the slice syntax that python provides (labs aren't iterable
        so it doesen't matter too much) we have a nice way of creating tasks
        starting with name then type and optionally the arguments r_commandequired for the
        Task instance being created.

        :key: Slice
        * start, stop, and step respectively
        :name: String
        :task_type: Type identifier for desired Task type
        :args: List
        :return: None
        """
        if isinstance(key, slice):
            name, task_type, args = key.start, key.stop, key.step
            if not self.tasks.has_key(name) and issubclass(task_type, Tasks.Task):
                task = task_type() if args == None else task_type(*args)
                self.tasks[name] = task
                return task
            #elif self.tasks.has_key(name):
            #    # task already defined error, ida know
            elif not issubclass(task_type, Tasks.Task):
                raise TypeError("Task_type must be a subclass or instance of Task")

    def __call__(self, query, incremental = True, **kwargs):
        """
        This can be used to select files. Its pretty much just a wrapper for
        Utilities.select except it helps if you want to do some incremental stuff.

        :query: String
        :incremental: Boolean
        :kwargs: Mapping
        """
        if incremental:
            kwargs.update(runtime = self.settings.runtime)
        return Utilities.select(query, **kwargs)

    @property
    def tasks(self):
        """
        Standard property stuff just exists so that any subclasses can define
        custom behaviours for getters and setters.

        :return: Dictionary
        """
        return self.__tasks

    @property
    def settings(self):
        """
        Standard property stuff just exists so that any subclasses can define
        custom behaviours for getters and setters.

        :return: Settings
        """
        return self.__settings

    def exit(self):
        """
        This is called when the lab has finished processing (look in main)
        doesen't do much and should scarcely be called by the user

        :return: None
        """
        self.settings.runtime = Utilities.time_stamp()
        self.settings.save()

    def main(self, args = None):
        """
        This is the main function and should always be called if the user
        wants to interact with the build using the commandline.
        otherwise all it does is call exit for you. In theory you coud omit main
        and use exit instead if you don't want to interact with the build in any way
        but the exit process is crucial in that it saves the runtime to the settings
        so that the incremental selection functions properly.

        :args: List
        :return: None
        """
        args = parser.parse_known_args(args = args)[0]
        if args.routine:
            if isinstance(self.tasks[args.routine], Tasks.Task):
                self.tasks[args.routine](self)
        self.exit()

    def __init__(self, settings_dir = shutil.os.getcwd()):
        """
        Yep, here's the intializer. just sets up the settings/loads them if they
        already exist, adds builtins. Thats all she/he/they/it wrote.

        :settings_dir: String
        :return: lab
        """
        settings_path = shutil.os.path.join(settings_dir, "settings")
        if shutil.os.path.exists(settings_path) and shutil.os.path.isfile(settings_path):
            self.__settings = Utilities.Settings.load(settings_dir)
        else:
            self.__settings = Utilities.Settings(directory = settings_dir)
            self.settings.runtime = 0
        Tasks.add_builtins(self)

# move docstrings into spinx and finish current documentation and tests
# once that is done try and configure github pages with jekyll
# or hugo to make a nice project page
# then start C submodule
