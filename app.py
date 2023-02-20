import json
import dateutil.parser
import babel
from flask import (
  Flask, 
  render_template, 
  request, 
  Response, 
  flash, 
  redirect, 
  url_for, 
  abort)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_migrate import Migrate
from logging import Formatter, FileHandler
from flask_wtf import Form
import sys
from datetime import datetime
from models import db, Campaigns, Creators, Publisher


# App configuration

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db.init_app(app)
debug = True

migrate = Migrate(app, db)


# Filter

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime


# Routes 

@app.route('/')
def home():
    return render_template('home/index.html')

#Creators Profile route

@app.route('/profile/<int:creator_id>', methods=['GET'])
def view_profile(creator_id):

    profile = Creators.query.get_or_404(creator_id)


    return render_template('home/profile.html', profile=profile)

# Creators list only for publishers

#@app.route('/creators/', methods=['GET'])
#def list_creators():

#    return render_template('home/creators.html')

# Publishers Profile route

@app.route('/publishers-profile/<int:publisher_id>', methods=['GET'])
def view_publisher_profile(publisher_id):

    publisher_profile = Publisher.query.get_or_404(publisher_id)

    campaigns_created = Campaigns.query.filter_by(id_publisher = publisher_id).count()
    print (campaigns_created)


    return render_template('home/publishers-profile.html', profile=publisher_profile, campaigns = campaigns_created)


# Publisher routes. Publishers could only see their own campaigns

@app.route('/campaigns', methods=['GET'])
def list_campaigns():

   campaign = Campaigns.query.all()
   


   return render_template('home/campaigns.html', campaing=campaign)



#@app.route('/campaigns', methods=['POST'])
#def create_campaign():

#@app.route('/campaigns/<int:id_campaing', methods=['DELETE'])
#def delete_campaign(id_campaign):


# Creators routes. Creators can see all campaigns in orther to apply

#@app.route('/campaigns', methods=['GET'])
#def list_all_campaigns():


#@app.route('/campaigns/<int:id_campaign>', methods=['PATCH'])
#def apply_campaign(id_campaign):


#Error handlers

@app.errorhandler(403)
def not_found_error(error):
    return render_template('home/page-403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('home/page-500.html'), 500



# Default port and launch

if __name__ == "__main__":
    app.run(debug=True)

