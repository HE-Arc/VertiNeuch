=====
Usage
=====

To use VertiNeuch in a project, add it to your `INSTALLED_APPS`:

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
