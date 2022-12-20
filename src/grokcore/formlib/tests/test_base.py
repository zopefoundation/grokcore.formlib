import doctest
import re
import unittest
import zope.component.eventtesting

from pkg_resources import resource_listdir
from zope.testing import cleanup, renormalizing


def setUpZope(test):
    zope.component.eventtesting.setUp(test)


def cleanUpZope(test):
    cleanup.cleanUp()


checker = renormalizing.RENormalizing([
    # str(Exception) has changed from Python 2.4 to 2.5 (due to
    # Exception now being a new-style class).  This changes the way
    # exceptions appear in traceback printouts.
    (re.compile(
        r"ConfigurationExecutionError: <class '([\w.]+)'>:"),
        r'ConfigurationExecutionError: \1:')])


def suiteFromPackage(name):
    layer_dir = 'base'
    files = resource_listdir(__name__, f'{layer_dir}/{name}')
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.formlib.tests.{}.{}.{}'.format(
            layer_dir, name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            setUp=setUpZope,
            tearDown=cleanUpZope,
            checker=checker,
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2))
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['form']:
        suite.addTest(suiteFromPackage(name))
    return suite
