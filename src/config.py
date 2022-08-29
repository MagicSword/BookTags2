import os


# project setting
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Project Setting
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # SQLAlchemy setting
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "booktags.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Mail setting
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["your-email@example.com"]
