=================
How to contribute
=================

Prime directives: Privacy, Hackability
======================================

Searx has two prime directives, **privacy-by-design and hackability** .  The
hackability comes in three levels:

- support of search engines
- plugins to alter search behaviour
- hacking searx itself

Note the lack of "world domination" among the directives.  Searx has no
intention of wide mass-adoption, rounded corners, etc.  The prime directive
"privacy" deserves a separate chapter, as it's quite uncommon unfortunately.

Privacy-by-design
-----------------

Searx was born out of the need for a **privacy-respecting** search tool which
can be extended easily to maximize both, its search and its privacy protecting
capabilities.

A few widely used features work differently or turned off by default or not
implemented at all **as a consequence of privacy-by-design**.

If a feature reduces the privacy preserving aspects of searx, it should be
switched off by default or should not implemented at all.  There are plenty of
search engines already providing such features.  If a feature reduces the
protection of searx, users must be informed about the effect of choosing to
enable it.  Features that protect privacy but differ from the expectations of
the user should also be explained.

Also, if you think that something works weird with searx, it's might be because
of the tool you use is designed in a way to interfere with the privacy respect.
Submitting a bugreport to the vendor of the tool that misbehaves might be a good
feedback to reconsider the disrespect to its customers (e.g. ``GET`` vs ``POST``
requests in various browsers).

Remember the other prime directive of searx is to be hackable, so if the above
privacy concerns do not fancy you, simply fork it.

  *Happy hacking.*

Code
====

.. _PEP8: https://www.python.org/dev/peps/pep-0008/


In order to submit a patch, please follow the steps below:

- Follow coding conventions.

  - PEP8_ standards apply, except the convention of line length
  - Maximum line length is 120 characters

- Check if your code breaks existing tests.  If so, update the tests or fix your
  code.

- If your code can be unit-tested, add unit tests.

- Add yourself to the :origin:`AUTHORS.rst` file.

- Create a pull request.

For more help on getting started with searx development, see :ref:`devquickstart`.


Translation
===========

Translation currently takes place on :ref:`transifex <translation>`.

.. caution::

   Please, do not update translation files in the repo.


Documentation
=============

.. _Sphinx: http://www.sphinx-doc.org
.. _reST: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

.. sidebar:: The reST sources

   has been moved from ``gh-branch`` into ``master`` (:origin:`docs`).

The documentation is built using Sphinx_.  So in order to be able to generate
the required files, you have to install it on your system.  Much easier, use
Makefile our targets.

Here is an example which makes a complete rebuild:

.. code:: sh

   $ make docs-clean docs
   ...
   The HTML pages are in dist/docs.


live build
----------

.. sidebar:: docs-clean

   It is recommended to assert a complete rebuild before deploying (use
   ``docs-clean``).

Live build is like WYSIWYG, If you want to edit the documentation, its
recommended to use.  The Makefile target ``docs-live`` builds the docs, opens URL
in your favorite browser and rebuilds every time a reST file has been changed.

.. code:: sh

   $ make docs-live
   ...
   The HTML pages are in dist/docs.
   ... Serving on http://0.0.0.0:8080
   ... Start watching changes



deploy on github.io
-------------------

To deploy documentation at :docs:`github.io <.>` use Makefile target
``gh-pages``, which will builds the documentation, clones searx into a sub
folder ``gh-pages``, cleans it, copies the doc build into and runs all the
needed git add, commit and push:

.. code:: sh

   $ make docs-clean gh-pages
   ...
   SPHINX    docs --> file://<...>/dist/docs
   The HTML pages are in dist/docs.
   ...
   Cloning into 'gh-pages' ...
   ...
   cd gh-pages; git checkout gh-pages >/dev/null
   Switched to a new branch 'gh-pages'
   ...
   doc available at --> https://asciimoo.github.io/searx