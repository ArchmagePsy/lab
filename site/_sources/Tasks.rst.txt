*****
Tasks
*****
In this module all the basic tasks and :ref:`task-obj` are defined.
They're the basic components of pretty much any script and they act
as glorified functions only they can do some nice stuff
like parsing commandline arguments to override the parameters passed to them or
in the case of the CLI this is the only way to pass arguments to them.

.. _task-obj:

The ``Task`` object
###################
Instances or subclasses of this can be found in :ref:`lab-obj` 's :ref:`tasks-prop`
I guess if you're used to make you could call them targets  however there is no way
to specify dependencies for them but thats not really a big issue (IMO)
as you can call other tasks whenever you want.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Task()

.. _parser-prop:

``parser`` property
********************
Standard property stuff. Just defines read-only access to the parser seen as
it is kind of crucial to the task working properly however the developer will still
be able to make changes to it as they would any ``ArgumentParser``.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Task()
  my_task.property # ArgumentParser at blah blah

.. _task-function-prop:

``task_function`` property
**************************
A getter and setter for the ``__task_function`` member. This is the
function bound to the Task's ``__call__`` method. It should recieve a project and
optionally an args list and whatever custom arguments are required.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Task()
  my_task.task_function = lambda project: "uhhhh"
  my_task(None) # uhhhh

.. _define-meth:

``define`` method
*****************
All this does is set :ref:`task-function-prop` to the parameter ``func``
which allows the developer to define tasks with a decorator.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Task()
  @my_task.define
  def foo(project):
    return "uhhhh"
  my_task(None) # uhhhh

.. _undefined-task-error-ex:

The ``UndefinedTaskError`` Exception
####################################
Just a custom exception for tasks where the :ref:`task-function-prop` is not defined
(``None``)

.. code-block:: python

  from Lab import Tasks

  try:
    my_task = Tasks.Task()
    my_task()
  except Tasks.UndefinedTaskError as Err:
    print "whoops"

.. _command-task:

The ``Command`` Task
######################
This is a child of :ref:`task-obj` and makes using commands, say for example ``rm``,
easier by doing all of the subprocess and argument stuff for you. if in :ref:`command-prop`
you use python's named string formatting it will detect this and add it to the :ref:`parser-prop`

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Command("echo 'hello world'")

.. _command-prop:

``command`` property
********************
this is used to set/get the ``__command`` member. The setter automatically calls
the :ref:`setup-parser-meth` which will look for any named arguments and add them
to the :ref:`parser-prop` .

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Command("echo 'hello world'")
  my_task.command # "echo 'hello world'"
  my_task.command = "echo 'good bye'"

.. _setup-parser-meth:

``setup_parser`` method
***********************
This method is called whenever the :ref:`command-prop` is updated and it sets up
the :ref:`parser-prop` (duh) currently its kinda messy and in the future I hope to
optimize it but at least for now it works.

.. code-block:: python

  from Lab import Tasks

    my_task = Tasks.Command("echo 'hello world'")
    my_task.setup_parser()

.. _clean-cmd:

The ``Clean`` Command
#####################
Currently I only have one predefined task, the Clean Command, give it a directory
and it'll remove everything in it. At the moment it just uses a wildcard but I'm
planning on making it selective/incremental in some way I.e removes all of
the objects whose corresponding sources have been removed.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Clean()
  my_task(None, directory = "directory/to/clean")
  """
  say good bye to all those files!
  (on linux) eventually I'll make it Xplatform
  """

.. _routine-task:

The ``Routine`` Task
####################
I initially made this before I had figured out the entire argparse thing but decided
to keep it as developers might want to use it. It just functions as a Task that
takes no input other than the ``project``.

.. code-block:: python

  from Lab import Tasks

  my_task = Tasks.Routine()
  # pretty much the same except no kwargs or args

.. _add-builtins-func:

The ``add_builtins`` function
#############################
This is called in the initializer of :ref:`lab-obj` it just adds all the basic tasks
defined here (only :ref:`clean-cmd` is currently added) but alas In the future
when I've added more tasks/commands it will be more useful.

.. code-block:: python

  from Lab import lab, Tasks

  my_lab = lab()
  Tasks.add_builtins(my_lab)
  """
  this will make no difference because
  the initializer for lab already does this
  """
