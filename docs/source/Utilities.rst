*********
Utilities
*********
These aren't really important to the general developer as :ref:`lab-obj`
does all the heavy lifting for them but these are here just in case :P.

.. _settings-obj:

The ``Settings`` object
#######################
This is the object that can be found in :ref:`lab-obj` 's :ref:`settings-prop`.
as stated there it is used to store persistent data and can be
loaded and saved with ease.

.. code-block:: python

  from Lab import Utilities

  settings = Utilities.Settings(directory = "/path/to/the/settings-directory")
  # like settings_dir in Lab.lab it defaults to current directory

.. _save-meth:

``save`` method
***************
This is the method used to save the data to the ``directory``
provided through the initializer as an optional argument
that defaults to ``shutil.os.getcwd()``. The pickle module is used
for serializing :ref:`settings-obj` .

.. code-block:: python

  from Lab import Utilities

  settings = Utilities.Settings()
  settings.save()

Nothing needs to be passed to this method because :ref:`settings-obj` already knows
which directory to use.

.. _load-meth:

``load`` method
***************
The load method is static and basically does
the reverse of the :ref:`save-meth`.
Only difference is it requires a directory as its only parameter.

.. code-block:: python

  from Lab import Utilities

  Utilities.Settings.load("/directory/where/Settings-file/is")

unlike its saving counterpart it requires a directory parameter.

.. _search-until-func:

The ``search_until`` function
#############################
This is used by :ref:`binary-search-func` to collect all
the remaining occurences of ``target`` in the ``array``.

.. code-block:: python

  from Lab import Utilities

  Utilities.search_until([1, 1, 1, 2, 1], 1)
  # [1, 1, 1]
  Utilities.search_until([(1, 2), (1, 3), (2, 4), (1, 5)], 1, key = lambda item: item[0])
  # [(1, 2), (1, 3)]

The function specified by the optional ``key`` parameter is called on each iteration
of ``array`` and then compared against the target.

.. _binary-search-func:

The ``binary_search`` function
##############################
This function is used by :ref:`select-func` to search the directories quickly
but can be used by the developer wherever they believe it necessary
although better implementations than mine probably exist.

.. code-block:: python

  from Lab import Utilities

  Utilities.binary_search([1, 2, 2, 2, 3, 4, 4, 5], 4)
  # [4, 4]
  Utilities.binary_search([(1, 2), (1, 4), (2, 2), (2, 4)], 2, key = lambda item: item[0])
  # [(2, 2), (2, 4)]

.. _set-env-func:

The ``set_env`` function
########################
Not really useful at all yet but kept for the sake of it

.. code-block:: python

  from Lab import Utilities

  Utilities.set_env("foo", 1)
  # sets environment variable "foo" to "1"

.. _get-env-func:

The ``get_env`` function
########################
Same as :ref:`set-env-func`

.. code-block:: python

  from Lab import Utilities

  Utilities.get_env("foo")
  # gets environment variable "foo"

.. _sort-by-func:

The ``sort_by`` function
########################
Serves as a wrapper around python's ``sort`` function
and may become useful in later versions.
(Was originally created for searching the horrible Resource system)

.. code-block:: python

  from Lab import Utilities

  Utilities.sort_by([2, 3, 1, 5, 4])
  # [1, 2, 3, 4, 5]

The ``by`` parameter makes things a little more complex. It basically takes a string
and calls ``getattr`` on all items of the given array, for example:

.. code-block:: python

  Utilities.sort_by(array, by = "foo")

would roughly translate to:

.. code-block:: python

  sorted(array, key = lambda item: getattr(item, by) if hasattr(item, by) else None)

I'll let you figure out which is easier.

.. _mutate-dict-func:

The ``mutate_dict`` function
############################
A helper function that works like ``map`` except for dictionaries

.. code-block:: python

  from Lab import Utilities

  Utilities.mutate_dict(lambda key, value: value + 1, {"foo": 1, "bar": 1})
  # {"foo": 2, "bar": 2}

This was ripped straight from my tests.

.. _filter-dict-func:

The ``filter_dict`` function
############################
A helper function that works like ``filter`` except for dictionaries

.. code-block:: python

  from Lab import Utilities

  Utilities.filter_dict(lambda key, value: bool(value), {"foo": 1, "bar": None})
  # {"foo": 1}

Again. Ripped straight from the tests. Why should I write another example
when I already have a perfectly good one?

.. _time-stamp-func:

The ``time_stamp`` function
###########################
Used to get the current time for :ref:`lab-obj` 's runtime setting.

.. code-block:: python

  from Lab import Utilities

  Utilities.time_stamp()
  # the time in milliseconds since computers started counting

.. _select-func:

The ``select`` function
#######################
Used by :ref:`lab-obj` to get the paths for the files
specified by ``query`` within the project tree. It defaults
to searching by filename where the suffix is omitted.

.. code-block:: python

  from Lab import Utilities

  Utilities.select("foo")
  """
  [all files with the name 'foo' in every folder
  starting from the current working directory]
  """
  Utilities.select("foo", runtime = my_lab.settings.runtime)
  """
  [all files with the name 'foo' that were updated
  since the runtime specified by 'my_lab']
  """
  import os
  Utilities.select(".py", key = lambda item: os.path.splitext(os.path.basename(item))[1])
  # [all files with the extension '.py']
  Utilities.select("foo", root = "src")
  # [all files starting from the 'src' directory withe the name 'foo']
