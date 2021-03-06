#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


AUTHOR = u'Kristoffer Dalby'
SITENAME = u'kradalby.no'
AUTHOR_EMAIL = u'kradalby@kradalby.no'


TIMEZONE = 'Europe/Oslo'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE_FORMAT = '%d/%m/%y - %X'
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'



READERS = {'html': None}

# Blogroll
# LINKS =  ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


SITEURL = 'https://kradalby.no'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

THEME = "./theme2"
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}


PLUGIN_PATHS = ['plugins']
PLUGINS = ['extract_toc', 'gravatar', 'render_math']


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = u"UA-18856525-15"
GITHUB = u"kradalby"
TWITTER = u"kradalby"


MD_EXTENSIONS = ['toc','codehilite(css_class=highlight)', 'extra']


# To override standard values use localconf.py!


import os, sys

if os.path.isfile("localconf.py"):
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    try: 
        exec("from localconf import *")
    except ImportError as e:
        print("Coult not import localconf: %s" % str(e))
    
