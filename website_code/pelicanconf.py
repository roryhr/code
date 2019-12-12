AUTHOR = 'Rory Hartong-Redden'
SITENAME = "Rory's Corner"

SITEURL = 'http://roryhr.com'

INDEX_SAVE_AS = 'articles.html'

# TEMPLATE_PAGES = {'images/donuts.html': '/pages/donuts.html'}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Home', '/'),
    ('Articles', '/articles'),
    ('Archives', '/archives'),
    ('About', '/pages/about'),
    ('Projects', '/pages/projects'),
    ('Contact', '/pages/contact'),
    ('Donuts', '/pages/donuts'),
]

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images']


TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = [
    ('BayPIGies', 'http://baypiggies.net/'),
    ('Pyninsula', 'http://pyninsula.org/'),
    ('SF Python', 'http://sfpythonmeetup.com/'),
    ('No Free Hunch (Kaggle)', 'http://blog.kaggle.com/'),
    ('EFAVDB', 'http://efavdb.com/'),
    ('MultiThreaded', 'http://multithreaded.stitchfix.com/'),
    ('SISL', 'http://sisl.stanford.edu/'),
]

# Social widget
SOCIAL = [
    ('Github', 'https://github.com/roryhr'),
    ('LinkedIn', 'https://www.linkedin.com/in/rory-hartong-redden-18334356'),
    ('Twitter', 'https://twitter.com/rory_h_r'),
]

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Turn off Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
