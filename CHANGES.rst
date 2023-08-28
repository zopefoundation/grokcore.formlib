Changes
=======

4.0 (2023-08-28)
----------------

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.

- Drop support for Python 2.7, 3.4, 3.5, 3.6.


3.0.1 (2018-01-12)
------------------

- Rearrange tests such that Travis CI can pick up all functional tests too.

3.0.0 (2018-01-04)
------------------

- Python 3 compatibility.

1.11 (2016-06-20)
-----------------

- ``grok.action`` will now trigger validation errors
  ``RequiredMissing`` for required fields that not present at all in
  the request.

1.10.1 (2016-02-15)
-------------------

- Update tests.

1.10 (2015-04-01)
-----------------

- Forms now notify the ObjectEditedEvent instead of the ObjectModifiedEvent.

1.10a1 (2013-11-22)
-------------------

- Add compatibility for CSRF protection feature in zope.formlib.

1.9 (2012-05-01)
----------------

- Nothing changed yet.

1.8 (2010-11-03)
----------------

- The context directive now has its own default computation.

1.7 (2010-11-01)
----------------

- Update version requirements for martian, grokcore.component, grokcore.security
  grokcore.view.

1.6 (2010-10-18)
----------------

- Made package comply to zope.org repository policy.

- Update functional tests to zope.app.wsgi Browser instead of zope.app.testing
  one.

- Don't depend anymore on zope.app.zcmlfiles for tests.

1.5 (2009-12-13)
----------------

- Use zope.container instead of zope.app.container (in tests and in the
  configure.zcml).

- Fixed up missing dependencies and splitted regular and test dependencies.


1.4 (2009-09-17)
----------------

* Reflect the changes in ``grokcore.view`` 1.12 where ``View`` and ``CodeView``
  become a single ``View`` again. This reverts to the View situation of
  ``grokcore.formlib`` 1.1.

1.3 (2009-09-16)
----------------

* Remove the reference to the grok.View permission that is no longer in
  grokcore.security 1.2

* Use 1.0b1 versions.cfg in Grok's release info instead of a local
  copy; a local copy for all grokcore packages is just too hard to
  maintain.

1.2 (2009-07-20)
----------------

* Adapted tests to the grokcore.view split of View and CodeView.

* Fixed forms to use self.template.render() directly instead of using a
  removed private method from grokcore.view.

* Add grok.View permissions for functional tests.

1.1 (2009-01-07)
----------------

* Have GrokForm define an empty actions attribute by default, in order
  for "action-less" forms to work easily.

1.0 (2008-09-25)
----------------

* Created ``grokcore.formlib`` in July 2008 by factoring
  ``zope.formlib``-based components, grokkers and directives out of
  Grok.
