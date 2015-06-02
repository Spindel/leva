#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Klas Ljungmark'
SITENAME = 'Leva Ltd.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = None

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "theme"

HIDE_SIDEBAR = True
BOOTSTRAP_FLUID = False
SHOW_ARTICLE_CATEGORY = False
SHOW_ARTICLE_AUTHOR = False
SHOW_DATE_MODIFIED = False

# SITELOGO="jumbo.jpg"

BANNER="images/jumbo.jpg"
BANNER_SUBTITLE = "Oceans, not only water"
BANNER_ALL_PAGES = True


SUMMARY_MAX_LENGTH=None

DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS=False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
        ('In Detail', '/pages/in-detail.html'),
        ('SGMF', 'http://www.sgmf.info/'),
)



BOOTSTRAP_THEME="yeti"
BOOTSTRAP_NAVBAR_INVERSE=True

ABOUT_ME="""<div class='vcard'>
         <span class='fn'>Klas Ljungmark</span>
         <div class='org'>Leva Ltd.</div>
         <a class='email' href='mailto:klas@leva.blue'>klas@leva.blue</a>
         <div class="adr">
            <div class="street-address">123 Street Street</div>
            <span class="locality">London</span>,
            <abbr class="region" title="England">England</abbr>,
            <span class="postal-code">000 999</span>
            <div class="country-name">Great Britain</div>
        </div>
"""

DIRECT_TEMPLATES = ('index', ) # 'categories', 'authors', 'archives')
STATIC_PATHS = ("images", "static")
CUSTOM_CSS = 'static/custom.css'


TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
