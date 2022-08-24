from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

from flask_login import UserMixin

# project setting
from src import db
from src import login


# Models
class User(UserMixin, db.Model):
    """User: status about user"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        """Gravatar generate

        https://www.gravatar.com/avatar/md5-HASH?s=size

        Args:
            size (int): pixel size from 1 to 2048
        """
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/{}?d=robohash&s={}".format(digest, size)


class Post(db.Model):
    """Post: data about posts"""

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post {}>".format(self.body)


# Other functions
@login.user_loader
def load_user(id):
    """load user status"""
    return User.query.get(int(id))
