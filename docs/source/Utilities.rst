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

.. _save-meth:

``save`` method
***************
This is the method used to save the data to the ``directory``
provided through the initializer as an optional argument
that defaults to ``shutil.os.getcwd()``. The pickle module is used
for serializing :ref:`settings-obj` .

.. _load-meth:

``load`` method
***************
The load method is static and basically does
the reverse of the :ref:`save-meth`.
Only difference is it requires a directory as its only parameter.

.. _search-until-func:

The ``search_until`` function
#############################
This is used by :ref:`binary-search-func` to collect all
the remaining occurences of ``target`` in the ``array``.

.. _binary-search-func:

The ``binary_search`` function
##############################
This function is used by :ref:`select-func` to search the directories quickly
but can be used by the developer wherever they believe it necessary
although better implementations than mine probably exist.

.. _set-env-func:

The ``set_env`` function
########################
Not really useful at all yet but kept for the sake of it

.. _get-env-func:

The ``get_env`` function
########################
Same as :ref:`set-env-func`

.. _sort-by-func:

The ``sort_by`` function
########################
Serves as a wrapper around python's ``sort`` function
and may become useful in later versions.
(Was originally created for searching the horrible Resource system)

.. _mutate-dict-func:

The ``mutate_dict`` function
############################
A helper function that works like ``map`` except for dictionaries

.. _filter-dict-func:

The ``filter_dict`` function
############################
A helper function that works like ``filter`` except for dictionaries

.. _time-stamp-func:

The ``time_stamp`` function
###########################
Used to get the current time for :ref:`lab-obj` 's runtime setting.

.. _select-func:

The ``select`` function
#######################
Used by :ref:`lab-obj` to get the paths for the files
specified by ``query`` within the project tree. It defaults
to searching by filename where the suffix is omitted.
