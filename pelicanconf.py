import bulrush

AUTHOR = 'Idalmis Vaquero'
SITENAME = 'The California Map of Hazardous Waste Sites and Schools'
SITEURL = 'https://nesanders.github.io/cawastemap'

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

OUTPUT_PATH = 'docs/'
 
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

GITHUB_URL = 'https://github.com/nesanders/cawastemap'
# Turn off category pages - see https://stackoverflow.com/a/31884167
CATEGORY_SAVE_AS = ''

# Don't make an authors page
AUTHOR_SAVE_AS = ''
# Don't make a tags page
TAG_SAVE_AS = ''

# We must set `categories` below to avoid an `article_page` error
# see https://stackoverflow.com/a/72281950
PAGINATED_TEMPLATES = {
    'index': None, 
    'tag': None, 
    'category': None, 
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
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/hzw_sites.geojson': {'path': 'pages/hzw_sites.geojson'},
    'extras/hzw_near_schools.geojson': {'path': 'pages/hzw_near_schools.geojson'},
    'extras/private_schools.geojson': {'path': 'pages/private_schools.geojson'},
    'extras/public_schools.geojson': {'path': 'pages/public_schools.geojson'},
    'extras/calenviroscreen.geojson': {'path': 'pages/calenviroscreen.geojson'},
    'extras/charter_schools.geojson': {'path': 'pages/charter_schools.geojson'},
    'extras/leaflet-heat.js': {'path': 'pages/leaflet-heat.js'},
    'images/Screenshot_20221207_211102_CalEnviroScreen_Vernon.png': {'path': 'pages/CalEnviroScreen_Vernon.png'}
}

# Used to allow html includes in markdown
MARKDOWN = {
    'extensions': ['mdx_include', 'footnotes']
}
