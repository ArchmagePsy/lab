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

.. _tasks-prop:

``tasks`` property
******************
This provides a getter for the ``__tasks`` member.
if the developer should want to add any tasks they
should use the ``__getitem__`` function that overrides
python's slice syntax to make defining tasks easier
(and cooler).

.. _settings-prop:

``settings`` property
*********************
As before this serves as a getter for the ``__settings`` member.
the settings are where all of the lab's persistent data should be stored
such as runtimes

.. _exit-meth:

``exit`` method
***************
This is the method called when the lab is going through the exit stage.
It **must** be called whether through the :ref:`main-meth` or manually as it updates
the runtime and saves the settings

.. _main-meth:

``main`` method
***************
This method isn't required but if called it will start a CLI allowing the developer
to execute tasks with ease and once the type *exit* or *quit* it will break the
loop and call the :ref:`exit-meth` for them.
