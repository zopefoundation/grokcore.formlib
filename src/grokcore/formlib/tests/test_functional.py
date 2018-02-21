import doctest
import grokcore.formlib
import unittest
import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi

from pkg_resources import resource_listdir


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.formlib)


def suiteFromPackage(name):
    layer_dir = 'functional'
    files = resource_listdir(__name__, '{}/{}'.format(layer_dir, name))
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.formlib.tests.%s.%s.%s' % (
            layer_dir, name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            extraglobs=dict(getRootFolder=layer.getRootFolder),
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                doctest.REPORT_NDIFF +
                doctest.IGNORE_EXCEPTION_DETAIL))
        test.layer = layer
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['form']:
        suite.addTest(suiteFromPackage(name))
    return suite
