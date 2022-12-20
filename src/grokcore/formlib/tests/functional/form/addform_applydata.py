"""
We can use AddFrom.applyData to save changes to a newly created
object.  The object doesn't yet need to have the attributes that are
going to be set on it.

  >>> getRootFolder()["zoo"] = Zoo()

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

AddForm.applyData() sends an IObjectModifiedEvent after having
modified the object.  Its return value is True in a Boolean sense when
the object has been modified:

  >>> browser.open("http://localhost/zoo/@@addmammoth")
  >>> browser.getControl(name="form.name").value = "Ellie the Mammoth"
  >>> browser.getControl(name="form.size").value = "Really small"
  >>> browser.getControl("Add entry").click()
  An IObjectModifiedEvent was sent for a mammoth with the following changes:
  IMammoth: name, size
  >>> print(browser.contents)
  There were changes according to applyData.

  >>> browser.open("http://localhost/zoo/ellie")
  >>> print(browser.contents)
  Hi, my name is Ellie the Mammoth, and I\'m "Really small"

"""
from zope import schema
from zope.container.btree import BTreeContainer
from zope.container.interfaces import IContainer
from zope.interface import Interface
from zope.interface import implementer
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

import grokcore.formlib as grok


class Zoo(grok.testing.Model, BTreeContainer):
    grok.testing.protect_get(grok.Public, *IContainer)


class IMammoth(Interface):
    name = schema.TextLine(title="Name")
    size = schema.TextLine(title="Size")


@implementer(IMammoth)
class Mammoth(grok.testing.Model):
    grok.testing.protect_get(grok.Public, 'name', 'size')
    grok.testing.protect_set(grok.Public, 'name', 'size')


class Index(grok.View):
    grok.context(Mammoth)

    def render(self):
        return 'Hi, my name is {}, and I\'m "{}"'.format(self.context.name,
                                                         self.context.size)


class AddMammoth(grok.AddForm):
    grok.context(Zoo)

    form_fields = grok.AutoFields(IMammoth)

    @grok.action('Add entry')
    def add(self, **data):
        self.context['ellie'] = ellie = Mammoth()
        if self.applyData(ellie, **data):
            return 'There were changes according to applyData.'
        return 'There were no changes according to applyData.'


@grok.subscribe(Mammoth, IObjectModifiedEvent)
def notify_change_event(mammoth, event):
    print("An IObjectModifiedEvent was sent for a mammoth with the "
          "following changes:")
    for descr in event.descriptions:
        print(descr.interface.__name__ + ": " + ", ".join(descr.attributes))
