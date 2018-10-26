#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year
AUTHOR = u'WebteamDIAG'
SITENAME = u'DIAG Base'
SITENAME_SHORT = 'DIAG'
SITE_PICTURE = 'images/computational_pathology_social_image.png'
SITEURL = ''

PATH = 'content'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'highlights/{slug}/'
ARTICLE_SAVE_AS = 'highlights/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

INDEX_SAVE_AS = 'highlights/index.html'

# Theme settings
THEME = "themes/pathology-theme"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil"]

# Other
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-pathology/edit/master/{file_path}'
