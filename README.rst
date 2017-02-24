=============================
VertiNeuch
=============================

.. image:: https://badge.fury.io/py/VertiNeuch.svg
    :target: https://badge.fury.io/py/VertiNeuch

.. image:: https://travis-ci.org/thegazou/VertiNeuch.svg?branch=master
    :target: https://travis-ci.org/thegazou/VertiNeuch

.. image:: https://codecov.io/gh/thegazou/VertiNeuch/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/thegazou/VertiNeuch

Vertineuch est une plateforme qui réunit des offres d'activités proposées par des guides de montagne et moniteurs d'escalade de la région neuchâteloise et jurassienne afin de répondre à la demande croissante pour l'escalade en salle et les activités se déroulant en pleine nature.

Documentation
-------------

The full documentation is at https://VertiNeuch.readthedocs.io.

Quickstart
----------

Install VertiNeuch::

    pip install VertiNeuch

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'VertiNeuch.apps.VertineuchConfig',
        ...
    )

Add VertiNeuch's URL patterns:

.. code-block:: python

    from VertiNeuch import urls as VertiNeuch_urls


    urlpatterns = [
        ...
        url(r'^', include(VertiNeuch_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
