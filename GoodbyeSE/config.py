import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = "bacditamtrungditamnamditam"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
# SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
# SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
# APP_NAME = "My App Name"
APP_NAME = "Goodbye SE"

# Uncomment to setup Setup an App icon
# APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
# AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
# AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
# OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Pt Brazil"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "pl": {"flag": "pl", "name": "Polish"},
}
# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css" # 2
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css" # 3
APP_THEME = "flatly.css" # 1
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"
# APP_THEME = "slate.css" # 4
# APP_THEME = "spacelab.css" # 5
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"

FAB_ROLES = {
    "Nhân viên": [
        [".*", "menu_access"],
        
        ["NhanVienView", "can_list"],
        ["NhanVienView", "can_show"],
        ["NhanVienView", "can_access"],
        ["NhanVienView", "menu_access"],
        ["NhanVienView", "can_edit"],
        
        ["LuongNhanVienView", "can_list"],
        ["LuongNhanVienView", "can_show"],
        ["LuongNhanVienView", "can_access"],
        ["LuongNhanVienView", "menu_access"],
        
        ["PhuCapView", "can_list"],
        ["PhuCapView", "can_show"],
        ["PhuCapView", "can_access"],
        ["PhuCapView", "menu_access"],
        
        ["LuongView", "can_list"],
        ["LuongView", "can_show"],
        ["LuongView", "can_access"],
        ["LuongView", "menu_access"],
        
        ["KhauTruView", "can_list"],
        ["KhauTruView", "can_show"],
        ["KhauTruView", "can_access"],
        ["KhauTruView", "menu_access"],
        
        ["LamViecView", "can_list"],
        ["LamViecView", "can_show"],
        ["LamViecView", "can_access"],
        ["LamViecView", "menu_access"],
        
        ["LichLamView", "can_list"],
        ["LichLamView", "can_show"],
        ["LichLamView", "can_access"],
        ["LichLamView", "menu_access"],
        
        ["DonXinNghiView", "can_list"],
        ["DonXinNghiView", "can_show"],
        ["DonXinNghiView", "can_access"],
        ["DonXinNghiView", "menu_access"],
        ["DonXinNghiView", "can_edit"],
        ["DonXinNghiView", "can_add"],
        ["DonXinNghiView", "can_delete"],
        
        ["UserDBModelView","can_userinfo"]
    ],
    # "Public": [
    #     ["PublicView", "can_list"],
    #     ["PublicView", "can_show"],
    #     ["PublicMenu", "menu_access"]
    # ]
}
