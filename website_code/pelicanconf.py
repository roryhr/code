AUTHOR = "Rory Hartong-Redden"
SITENAME = "Rory's Corner"

SITEURL = "https://www.roryhr.com"

INDEX_SAVE_AS = "articles.html"

THEME = "themes/notmyidea"

# Comment out ANALYTICS during local development
ANALYTICS = """<script defer src="https://cloud.umami.is/script.js" data-website-id="a1db9ef4-135a-4406-8304-f1ffa50665bc"></script>"""

# TEMPLATE_PAGES = {'images/donuts.html': '/pages/donuts.html'}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ("Home", "/"),
    ("Articles", "/archives"),
    ("About", "/pages/about"),
    ("Projects", "/pages/projects"),
    ("Contact", "/pages/contact"),
    ("Donuts", "/images/donuts/donuts"),
]

PATH = "content"
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["blog"]
STATIC_PATHS = ["images"]


TIMEZONE = "America/Vancouver"

DEFAULT_LANG = "en"

# Blogroll
LINKS = [
    ("ChiPy", "https://www.chipy.org/"),
    ("BayPIGies", "http://baypiggies.net/"),
    ("Pyninsula", "http://pyninsula.org/"),
    ("SF Python", "http://sfpythonmeetup.com/"),
    ("No Free Hunch (Kaggle)", "http://blog.kaggle.com/"),
    ("EFAVDB", "http://efavdb.com/"),
    ("Where's Your Ed At", "https://www.wheresyoured.at/"),
    ("SISL", "http://sisl.stanford.edu/"),
    ("Advent of Code", "https://adventofcode.com/"),
    ("Simon Willison's Weblog", "https://simonwillison.net/"),
]

# Social widget
SOCIAL = [
    ("Github", "https://github.com/roryhr"),
    ("LinkedIn", "https://www.linkedin.com/in/rory-hartong-redden"),
    ("Mastodon", "https://mastodon.social/@roryhr"),
]

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Turn off Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
