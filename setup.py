import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
)

tests_require = [
    'zope.app.wsgi[test]',
    'zope.configuration',
    'zope.testbrowser',
    'zope.testing',
]

setup(
    name='grokcore.formlib',
    version='4.0.dev0',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grokcore.formlib',
    description='Grok-like configuration for zope.formlib components',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Zope :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'grokcore.component >= 2.1',
        'grokcore.content >= 1.2',
        'grokcore.security >= 1.5',
        'grokcore.view >= 2.0',
        'martian >= 0.13',
        'pytz',
        'zope.container',
        'zope.event',
        'zope.formlib >= 4.3.0a2.dev0',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.publisher',
        'zope.schema',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
