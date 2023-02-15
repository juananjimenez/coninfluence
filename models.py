from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

# Publisher definition

class Publisher(db.Model):
    __tablename__ = 'Publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(120))
    industry = db.Column(db.String(120))
    website = db.Column(db.String(120))
    email = db.Column(db.String(120))
    url_logo = db.Column(db.String(500))
    campaigns_lauched = db.relationship('Campaigns', backref='publisher', lazy='joined', cascade="all, delete")


# Creators definition

class Creators(db.Model):
    __tablename__ = 'Creators'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    nick_name = db.Column(db.String(120))
    url_picture = db.Column(db.String(120))
    email = db.Column(db.String(120))
    topics = db.Column(db.String(120))
    instagram = db.Column(db.String(120))
    tik_tok = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    twitter = db.Column(db.String(120))
    youtube = db.Column(db.String(120))
    total_followers = db.Column(db.Integer)
    campaigns_done = db.relationship('Campaigns', backref='creator', lazy='joined', cascade="all, delete")


# A publisher has many campaigns with different creators and the creator can access to multiples campaigns from different or same publishers

class Campaigns(db.Model):
    __tablename__ = 'Campaings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    start_date = db.Column(db.DateTime())
    last_date = db.Column(db.DateTime())
    budget = db.Column(db.Integer)
    sources = db.Column(db.String(250))
    description = db.Column(db.String)

    id_creator = db.Column(db.Integer, db.ForeignKey('Creators.id'), nullable=False)
    id_publisher = db.Column(db.Integer, db.ForeignKey('Publishers.id'), nullable=False)