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
