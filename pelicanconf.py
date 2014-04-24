#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kristoffer Dalby'
SITENAME = u'kradalby.no'

TIMEZONE = 'Europe/Oslo'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE_FORMAT = '%d/%m/%y - %X'
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


SITEURL = 'https://kradalby.no/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-18856525-15"
GITHUB_URL = "http://github.com/kradalby"
TWITTER_USERNAME = "kradalby"
