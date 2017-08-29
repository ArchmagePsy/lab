***
Lab
***
This is the module found in ``__init__.py``
and defines :ref:`lab-obj` which is the main part
of every build script as it contains all the tasks
required to automate aspects of a projects building/testing.

.. _lab-obj:

The ``lab`` object
##################
As described above this object will store all
the tasks defined by the developer and provide them
with a CLI when run to help them execute tasks in addition
to this it will also save the previous build's runtime
in order to make use of :ref:`select-func` 's
runtime parameter for use in incremental builds.

.. code-block:: python

  from Lab import lab

  my_lab = lab(settings_dir = "/path/to/your/project")
  # settings_dir defaults to the current directory which should be ok in most cases

the ``settings_dir`` parameter is passed to :ref:`settings-obj`
created as part of the lab.

.. _tasks-prop:

``tasks`` property
******************
This provides a getter for the ``__tasks`` member.
if the developer should want to add any tasks they
should use the ``__getitem__`` function that overrides
python's slice syntax to make defining tasks easier
(and cooler).

.. code-block:: python

  from Lab import lab, Tasks

  my_lab = lab()
  my_lab["the_task_name" : Tasks.Task : ["this list is passed to the Task's initializer"]]

The third parameter is optional and should only be used if
the Task has any arguments in its initializer. In order to access these tasks
you may either use the property of python's ``__getattr__``

.. code-block:: python

  from Lab import lab, Tasks

  my_lab = lab()
  my_lab["foo" : Tasks.Task]
  my_lab.foo(my_lab) # runs the task named 'foo'
  my_lab.tasks["foo"](my_lab) # same thing except done as a string

the former looks much nicer but the latter is there if you need it I.e only have
access to the string of a task's name for some reason.

.. _settings-prop:

``settings`` property
*********************
As before this serves as a getter for the ``__settings`` member.
the settings are where all of the lab's persistent data should be stored
such as runtimes

.. code-block:: python

  from Lab import lab

  my_lab = lab()
  my_lab.settings.foo = 1
  # VV never change these unless you know what you're doing VV
  my_lab.settings.directory = "" # not a valid directory
  my_lab.settings.runtime = 0 # now all files regardless of mtime will be selected

.. _exit-meth:

``exit`` method
***************
This is the method called when the lab is going through the exit stage.
It **must** be called whether through the :ref:`main-meth` or manually as it updates
the runtime and saves the settings

.. code-block:: python

  from Lab import lab

  my_lab = lab()
  my_lab.exit() # saves new runtime to settings

.. _main-meth:

``main`` method
***************
This method isn't required but if called it will start a CLI allowing the developer
to execute tasks with ease and once the type *exit* or *quit* it will break the
loop and call the :ref:`exit-meth` for them.

.. code-block:: python

  from Lab import lab

  my_lab = lab()

  if __name__ = "__main__":
    my_lab.main() # starts CLI and calls exit when finished

Its a good idea to put the call to :ref:`main-meth` inside an if like this
so that it doesen't get run if you import your build script from another file.
