#!/usr/bin/env python

"""markdown2: A fast and complete Python implementaion of Markdown.

Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML.  Markdown's text
format is most similar to that of plain text email, and supports
features such as headers, *emphasis*, code blocks, blockquotes, and
links.  -- http://daringfireball.net/projects/markdown/

This is a fast and complete Python implementation of the Markdown
spec.
"""

import sys
from distutils.core import setup

sys.path.insert(0, "lib")
import markdown2


classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Documentation
Topic :: Text Processing :: Filters
Topic :: Text Processing :: Markup :: HTML 
"""

if sys.version_info < (2, 3):
    # Distutils before Python 2.3 doesn't accept classifiers.
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(name="markdown2",
      version=markdown2.__version__,
      maintainer="Trent Mick",
      maintainer_email="trentm@gmail.com",
      url="http://code.google.com/p/python-markdown2/",
      license="http://www.opensource.org/licenses/mit-license.php",
      platforms=["any"],
      description=doclines[0],
      classifiers=filter(None, classifiers.split("\n")),
      long_description="\n".join(doclines[2:]),
      )

