import sys
import os
from distutils.core import setup

VERSION = '1.3.8'
py_vers_tag = '-%s.%s' % sys.version_info[:2]

test_dirs = ['functional_tests', 'unit_tests', os.path.join('doc','doc_tests'), 'nose']

from distutils.core import setup

addl_args = dict(
    packages = ['nose', 'nose.ext', 'nose.plugins', 'nose.sphinx',
                'nose.tools'],
    scripts = ['bin/nosetests'],
    )

setup(
    name = 'nose',
    version = VERSION,
    author = 'Jason Pellerin',
    author_email = 'jpellerin+nose@gmail.com',
    description = ('nose extends unittest to make testing easier'),
    long_description = \
    """nose extends the test loading and running features of unittest, making
    it easier to write, find and run tests.

    By default, nose will run tests in files or directories under the current
    working directory whose names include "test" or "Test" at a word boundary
    (like "test_this" or "functional_test" or "TestClass" but not
    "libtest"). Test output is similar to that of unittest, but also includes
    captured stdout output from failing tests, for easy print-style debugging.

    These features, and many more, are customizable through the use of
    plugins. Plugins included with nose provide support for doctest, code
    coverage and profiling, flexible attribute-based test selection,
    output capture and more. More information about writing plugins may be
    found on in the nose API documentation, here:
    http://readthedocs.org/docs/nose/

    If you have recently reported a bug marked as fixed, or have a craving for
    the very latest, you may want the development version instead:
    https://github.com/nose-devs/nose/tarball/master#egg=nose-dev
    """,
    license = 'GNU LGPL',
    keywords = 'test unittest doctest automatic discovery',
    url = 'http://readthedocs.org/docs/nose/',
    data_files = [('man/man1', ['nosetests.1'])],
    package_data = {'': ['*.txt',
                         'examples/*.py',
                         'examples/*/*.py']},
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing'
        ],
    **addl_args
    )

