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
