===============================
deeplearning2020
===============================

.. image:: https://travis-ci.com/into-ai/deeplearning2020.svg?branch=master
        :target: https://travis-ci.com/into-ai/deeplearning2020
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/deeplearning2020.svg
        :target: https://pypi.python.org/pypi/deeplearning2020
        :alt: PyPI version

.. image:: https://img.shields.io/github/license/into-ai/deeplearning2020
        :target: https://github.com/into-ai/deeplearning2020
        :alt: License

.. image:: https://codecov.io/gh/into-ai/deeplearning2020/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/into-ai/deeplearning2020
        :alt: Test Coverage

""""""""

Your short description here. `into-ai.github.io/deeplearning2020 <https://into-ai.github.io/deeplearning2020>`_

.. code-block:: console

    $ pip install deeplearning2020

See the `official documentation`_ for more information.

.. _official documentation: https://deeplearning2020.readthedocs.io

.. code-block:: python

    import deeplearning2020

Tests
~~~~~~~
You can run tests with

.. code-block:: console

    $ invoke test
    $ invoke test --min-coverage=90     # Fail when code coverage is below 90%
    $ invoke type-check                 # Run mypy type checks

Linting and formatting
~~~~~~~~~~~~~~~~~~~~~~~~
Lint and format the code with

.. code-block:: console

    $ invoke format
    $ invoke lint

All of this happens when you run ``invoke pre-commit``.

Note
-----

This project is still in the alpha stage and should not be considered production ready.
