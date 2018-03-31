#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rory Hartong-Redden'
SITENAME = "Rory's Corner"

# SITEURL = ''
# OUTPUT_PATH = 'output'

# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'),
             ('Articles', '/archives'),
             ('About', '/pages/about'),
             ('Projects', '/pages/projects'),
             ('Contact', '/pages/contact')]

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images']

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'


# Blogroll
LINKS = (('Keras', 'http://blog.keras.io/'),
         ('No Free Hunch (Kaggle)', 'http://blog.kaggle.com/'),
         ('EFAVDB', 'http://efavdb.com/'),
         ('Google', 'http://googleresearch.blogspot.com/'),
         ('DeepMind', 'https://deepmind.com/blog'),
         ('MultiThreaded', 'http://multithreaded.stitchfix.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/roryhr'),
          ('LinkedIn', 'https://www.linkedin.com/in/rory-hartong-redden-18334356'),
	      ('Twitter', 'https://twitter.com/rory_h_r'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


PLUGINS = ['render_math']

# Turn off Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
