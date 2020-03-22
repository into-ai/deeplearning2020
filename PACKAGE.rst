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

Begleitendes Python Package zum Kurs `Eine praktische Einführung in Deep Learning für Computer Vision <https://open.hpi.de/courses/neuralnets2020>`_ auf `OpenHPI <https://open.hpi.de/>`_.

.. code-block:: console

    $ pip install --upgrade deeplearning2020

In einem ``jupyter notebook`` wie Google Colab geht das mit 

.. code-block:: python

    !pip install --upgrade deeplearning2020

Das Package enthält einige von uns bereitgestellte Hilfsfunktionen und erlaubt es euch, eure für die Übungen trainierten `keras` Modelle zur Bewertung abzugeben.

Nutzung der Hilfsfunktionen
------------------------------

.. code-block:: python

    from deeplearning2020 import helpers
    helpers.plot_predictions(...)  # Beispiel

Nutzung zur Übungsabgabe
------------------------------

.. code-block:: python

    from deeplearning2020 import Submission
    Submission('<token>', '<assignment-id>', model).submit()

Der ``<token>`` und die ``<assignment-id>`` wird dir für die Abgabe mitgeteilt.