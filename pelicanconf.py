#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrew Aitken'
SITENAME = u'Andrew Aitken'
SITESUBTITLE = u'Blog'
SITEURL = 'http://www.andrewaitken.com'
THEME = 'themes/coffee-code'

STATIC_PATHS = ['images', 'static', ]
EXTRA_PATH_METADATA = {
	'static/CNAME': {'path': 'CNAME'},
	'static/favicon.ico': {'path': 'favicon.ico'},
	'static/robots.txt': {'path': 'robots.txt'},
	'pages/404.md': {'path': '404.html'},
}

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Nice Urls
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = '{slug}.html}'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'


SITE_DESCRIPTION = "I am Andrew Aitken, a .net developer living in Glasgow."

# Blogroll
LINKS =  (('Cameron Fletcher', 'http://cameronfletcher.com/'),
	      ('Dougal Matthews', 'http://www.dougalmatthews.com/'),
		  ('Steven Gibson', 'https://twitter.com/sgxbsxn'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/AndyA13'),
          ('github', 'https://github.com/AndyA13'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
