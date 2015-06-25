#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGINS = ['pelican_commonmark']



AUTHOR = 'Klas Ljungmark'
SITENAME = 'LEVA Ltd.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'

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
        ('About Klas', '/pages/in-detail.html'),
#         ('SGMF', 'http://www.sgmf.info/'),
)



BOOTSTRAP_THEME="yeti"
BOOTSTRAP_NAVBAR_INVERSE=True

ABOUT_ME="""<div class='vcard'>
             <span class='fn'>Klas Ljungmark</span>
             <div class='org organization-name'>LEVA Ltd</div>
             <div class='org organization-unit'>Co. No: 09507255</div>
             <div class="adr">
                <div class="street-address">138 Marylebone Road</div>
                <span class="locality">London</span>,
                <span class="postal-code">NW1 5PH</span>
                <div class="country-name">Great Britain</div>
            </div>
            <a class='email' href='mailto:klas@leva.blue'>klas@leva.blue</a>
            <div class="tel">+44 7470 83 57 54</div>
            <div class="tel">+46 723 99 46 91</div>
            </div>
"""

DIRECT_TEMPLATES = ('index', ) # 'categories', 'authors', 'archives')
STATIC_PATHS = ("images", "static")
CUSTOM_CSS = 'static/custom.css'


TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
