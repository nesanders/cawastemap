import bulrush

AUTHOR = 'Idalmis Vaquero'
SITENAME = 'The California Map of Hazardous Waste Sites and Schools'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ()
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

OUTPUT_PATH = 'docs/'
 
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

GITHUB_URL = 'https://github.com/nesanders/cawastemap'
# Turn off category pages - see https://stackoverflow.com/a/31884167
# CATEGORY_SAVE_AS = ''

# Don't make an authors page
# AUTHOR_SAVE_AS = ''
# Don't make a tags page
# TAG_SAVE_AS = ''

# We must set `categories` below to avoid an `article_page` error
# see https://stackoverflow.com/a/72281950
PAGINATED_TEMPLATES = {
    'index': None, 
    'tag': None, 
    'category': 4, 
    'categories': None,
    'author': None
}

READERS = {'html': None, 'js': None}

STATIC_PATHS = [
    'images',
    'extras',
]
EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'custom.css'},
    'extras/CNAME': {'path': 'CNAME'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/hzw_sites.geojson': {'path': 'hzw_sites.geojson'},
    'extras/hzw_near_schools.geojson': {'path': 'hzw_near_schools.geojson'},
    'extras/private_schools.geojson': {'path': 'private_schools.geojson'},
    'extras/public_schools.geojson': {'path': 'public_schools.geojson'},
    'extras/calenviroscreen.geojson': {'path': 'calenviroscreen.geojson'},
    'extras/charter_schools.geojson': {'path': 'charter_schools.geojson'},
    'extras/leaflet-heat.js': {'path': 'leaflet-heat.js'},
}

# Used to allow html includes in markdown
MARKDOWN = {
    'extensions': ['mdx_include', 'footnotes']
}

# Add custom menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
# List these in reverse order - first item goes on right
MENUITEMS = (
    ('Full Report', '/cawastemap/report.html'),
    ('Executive Summary', '/cawastemap/exec-summary.html'),
    ('About', '/cawastemap'),
)

BULRUSH_SHOW_SUMMARY = True
LINKS = (
    ('Climate Justice Design Fellowship', 'https://projects.iq.harvard.edu/climatefellowship'),
    ('Communities for a Better Environment', 'https://www.cbecal.org')
)

SUMMARY_MAX_LENGTH = 500
