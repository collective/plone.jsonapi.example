plone.jsonapi.example
=====================

:Author:  Ramon Bartl
:Version: 0.1dev


.. contents:: Table of Contents
   :depth: 2


Introduction
------------

This example shows how to provide JSON API URLs for custom Dexterity_ content
types using plone.jsonapi.core_ and plone.jsonapi.routes_.


A simple Todo Content Type
--------------------------

A simple Dexterity_ based Todo content type is provided in `src/plone.todos`.
A `Todo` Item is basically an item with a `title` where the user can enter a
task, a `description`, where the user can add some additionaly notes and a
`completed` field, where the todo item can be completed.


The CRUD API
------------

The JSON API is defined in the `api` module of the `plone.todos` package.
It uses the `plone.jsonapi.routes` to provide the get, create, update and
delete functionality.


License
-------

MIT - do what you want


.. _Plone: http://plone.org
.. _Dexterity: https://pypi.python.org/pypi/plone.dexterity
.. _Werkzeug: http://werkzeug.pocoo.org
.. _plone.jsonapi.core: https://github.com/ramonski/plone.jsonapi.core
.. _plone.jsonapi.routes: https://github.com/ramonski/plone.jsonapi.routes
.. _mr.developer: https://pypi.python.org/pypi/mr.developer
.. _Utility: http://developer.plone.org/components/utilities.html
.. _CRUD: http://en.wikipedia.org/wiki/CRUD
.. _curl: http://curl.haxx.se/
.. _RESTful: http://en.wikipedia.org/wiki/Representational_state_transfer

.. vim: set ft=rst ts=4 sw=4 expandtab tw=78 :
