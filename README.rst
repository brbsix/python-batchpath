Python module to generate and verify pathnames meeting specified criteria.

About
===================

This module is sort of like os.walk on steroids. It was created to ease the use of command-line path arguments in your Python scripts. For instance, say the user passes in several files and directories as arguments and you want to return a sorted list of files within said directories meeting specific access, extension, and/or size criteria. Or perhaps the user passes in a list of files and you want to verify all of the files meet the necessary criteria before using them.


Documentation
=============

Installation
------------

::

   pip3 install batchpath

The :code:`batchpath` module is known to be compatible with Python 3.

NOTE: This module uses os.walk(), but will use scandir's significantly faster implementation if it is available. Consider installing the scandir module.

Usage
-----

.. code:: python

  from batchpath import GeneratePaths()

  gp = GeneratePaths()
  files = gp.files(['/path/to/directory'], access=os.R_OK, extensions=['conf','txt'], minsize=0, recursion=True)


.. code:: python

  from batchpath import VerifyPaths()

  vp = VerifyPaths()
  verified = vp.any(access=os.R_OK)

License
=======

Copyright (c) 2015 Six (brbsix@gmail.com).

Licensed under the GPLv2 license.


.. |travis| image:: https://travis-ci.org/magmax/python-readchar.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/python-readchar/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://pypip.in/v/readchar/badge.png
    :target: https://pypi.python.org/pypi/readchar
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/readchar/badge.png
    :target: https://pypi.python.org/pypi/readchar
    :alt: Number of PyPI downloads

.. _pypi: https://pypi.python.org/pypi/readchar
.. _GitHub: https://github.com/magmax/python-readchar
.. _python-inquirer: https://github.com/magmax/python-inquirer
.. _Travis: https://travis-ci.org/magmax/python-readchar
.. _Coveralls: https://coveralls.io/r/magmax/python-readchar
.. _@magmax9: https://twitter.com/magmax9

.. _the MIT license: http://opensource.org/licenses/MIT
.. _getch()-like unbuffered character reading from stdin on both Windows and Unix (Python recipe): http://code.activestate.com/recipes/134892/
.. _Danny Yoo: http://code.activestate.com/recipes/users/98032/
