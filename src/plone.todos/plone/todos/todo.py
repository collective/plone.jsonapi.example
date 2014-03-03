from five import grok
from zope import schema
from plone.dexterity.content import Container
from plone.directives import form
from plone.todos import MessageFactory as _


class ITodo(form.Schema):
    """ Todo Item
    """

    title = schema.TextLine(
        title=_(u"What to do?"))

    description = schema.Text(
        title=_(u"Notes"),
        required=False)

    completed = schema.Bool(
        title=_(u"Todo Completed"),
        default=False,
        required=False)


class Todo(Container):
    grok.implements(ITodo)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ITodo)
    grok.require('zope2.View')
