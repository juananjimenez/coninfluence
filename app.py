import json
import dateutil.parser
import babel
from flask import (
  Flask, 
  render_template, 
  request, 
  Response,
  jsonify, 
  flash, 
  redirect, 
  url_for, 
  abort)
from flask_moment import Moment
#from flask_cors import CORS
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
#CORS(app)
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

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route('/')
def home():
    return render_template('home/index.html')

#Creators Profile route

@app.route('/profile/<int:creator_id>', methods=['GET'])
def view_profile(creator_id):
  
        profile = Creators.query.get_or_404(creator_id)

        return render_template('home/profile.html', profile=profile)


# Creators Profile edit route

#@app.route('/profile/<int:creator_id', methods=['PATCH'])
#def edit_creator(creator_id):



# Creators list only for publishers

@app.route('/creators', methods=['GET'])
def list_creators():

    creators = Creators.query.all()

    return render_template('home/creators.html', creators=creators)

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


@app.route('/new-campaign', methods=['GET', 'POST'])
def create_campaign():

    error = False
    
    try:
        campaign = Campaigns (name = request.form.get('name'),
        start_date = request.form.get('end'),
        last_date = request.form.get('start'),
        budget = request.form.get('budget'),
        sources = request.form.get('social'),
        description = request.form.get('description'),
        creator = request.form.get('creator', ''),
        publisher = request.form.get('publisher', '')
        )
        print(campaign)
        db.session.add(campaign)
        db.session.commit()
    except: 
        db.session.rollback()
        
        error = True
        print(sys.exc_info())
    
    finally:
        db.session.close()

    return redirect(url_for('list_campaigns'))

    

@app.route('/campaigns/<int:campaign_id>/delete', methods=['GET', 'DELETE'])
def delete_campaign(campaign_id):
    
    try:
        Campaigns.query.filter_by(id = campaign_id).delete()
        db.session.commit()
        flash('The campaign has been deleted')
        return render_template('home/campaigns.html')
    
    except ValueError:
        flash('It was not possible to delete this campaign')
        db.session.rollback()
        
    finally:
        db.session.close()

    #return redirect(url_for('campaigns'))
       

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

