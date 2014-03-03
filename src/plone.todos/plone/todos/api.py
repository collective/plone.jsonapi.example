# -*- coding: utf-8 -*-

from plone.jsonapi.core import router

from plone.jsonapi.routes.api import url_for

# CRUD
from plone.jsonapi.routes.api import get_items
from plone.jsonapi.routes.api import create_items
from plone.jsonapi.routes.api import update_items
from plone.jsonapi.routes.api import delete_items


# GET TODOS
@router.add_route("/todos", "todos", methods=["GET"])
@router.add_route("/todos/<string:uid>", "todos", methods=["GET"])
def get(context, request, uid=None):
    """ get todos
    """
    items = get_items("plone.todos.todo", request, uid=uid, endpoint="todos")
    return {
        "url": url_for("todos"),
        "count": len(items),
        "items": items,
    }


# CREATE
@router.add_route("/todos/create", "todos_create", methods=["POST"])
@router.add_route("/todos/create/<string:uid>", "todos_create", methods=["POST"])
def create(context, request, uid=None):
    """ create todos
    """
    items = create_items("plone.todos.todo", request, uid=uid, endpoint="todos")
    return {
        "url": url_for("todos_create"),
        "count": len(items),
        "items": items,
    }


# UPDATE
@router.add_route("/todos/update", "todos_update", methods=["POST"])
@router.add_route("/todos/update/<string:uid>", "todos_update", methods=["POST"])
def update(context, request, uid=None):
    """ update todos
    """
    items = update_items("plone.todos.todo", request, uid=uid, endpoint="todos")
    return {
        "url": url_for("todos_update"),
        "count": len(items),
        "items": items,
    }


# DELETE
@router.add_route("/todos/delete", "todos_delete", methods=["POST"])
@router.add_route("/todos/delete/<string:uid>", "todos_delete", methods=["POST"])
def delete(context, request, uid=None):
    """ delete todos
    """
    items = delete_items("plone.todos.todo", request, uid=uid, endpoint="todos")
    return {
        "url": url_for("todos_delete"),
        "count": len(items),
        "items": items,
    }

# vim: set ft=python ts=4 sw=4 expandtab :
