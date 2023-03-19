#------------------------------------------#
# Imports
#------------------------------------------#


import json
import os
import dateutil.parser
import babel
from flask import (
  Flask, 
  render_template, 
  request,
  session, 
  Response,
  jsonify, 
  flash, 
  redirect, 
  url_for, 
  abort)
from flask_moment import Moment
from flask_cors import CORS
from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import Form
import sys
from datetime import datetime
from models import db, Campaigns, Creators, Publisher
from forms import *
from auth import AuthError, requires_auth
from os import environ as env
from urllib.parse import quote_plus, urlencode



# App configuration 1


app = Flask(__name__)
moment = Moment(app)
app.secret_key = env.get("APP_SECRET_KEY")
app.config.from_object('config')
db.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
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
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, PUT, DELETE, OPTIONS')
    return response

#--------------------------------------#
# Login & logout routes
#---------------------------------------#

@app.route('/login')
def login():
    AUTH0_AUTHORIZE_URL = "https://dev-p3lkca7jo6xho5o5.us.auth0.com/authorize?audience=coninfluence&response_type=token&client_id=TWJQz7GUeX3xAZRB9HYplTf7jsnrVHRp&redirect_uri=http://localhost:8080"
    return render_template('home/login.html', AUTH0_AUTHORIZE_URL = AUTH0_AUTHORIZE_URL)

@app.route('/')
def home():
    
    return render_template('home/index.html')

@app.route('/landing')
def landing():
    return render_template('home/landing.html')


#--------------------------------------#
# Creators routes
#---------------------------------------#

@app.route('/profile/<int:creator_id>', methods=['GET'])
#@requires_auth('get:profile')
def show_profile(creator_id):
  
    profile = Creators.query.get_or_404(creator_id)
    
    if not profile:
        abort(404)
  
    return render_template('home/profile.html', profile=profile)

# Creators list only for publishers

@app.route('/creators', methods=['GET'])
#@requires_auth('get:creators')
def list_creators():

    creators = Creators.query.all()

    return render_template('home/creators-list.html', creators=creators)


# New Creator

@app.route('/creators/new', methods=['GET'])
#@requires_auth('get:creator-profile')
def new_creator_form():
  form = CreatorForm()

  return render_template('forms/new-creator.html', form=form)


@app.route('/creators/new', methods=['POST'])
#@requires_auth('post:creator-profile')
def new_creator_submit():
    error = False
    form = CreatorForm()

    try: 
        first_name = form.first_name.data
        last_name = form.last_name.data
        nick_name = form.nick_name.data
        url_picture = form.url_picture.data
        email = form.email.data
        topics = form.topics.data
        instagram = form.instagram.data
        tik_tok = form.tik_tok.data
        facebook = form.facebook.data
        twitter = form.twitter.data
        youtube = form.youtube.data
        total_followers = form.total_followers.data

        creator = Creators(first_name = first_name, last_name = last_name, nick_name = nick_name, url_picture = url_picture, email = email, topics = topics,
        instagram = instagram, tik_tok = tik_tok, facebook = facebook, twitter = twitter, youtube = youtube, total_followers = total_followers)
        
        db.session.add(creator)
        flash('Creator ' + form.nick_name.data + ' was successfully listed!')
        db.session.commit()
  
    except:
        db.session.rollback()
        error = True
        
    finally:
        db.session.close()

    return render_template('forms/new-creator.html', form=form)   

# Edit creator profile

@app.route('/creator/<int:creator_id>/edit', methods= ['GET'])
#@requires_auth('get:creator-profile')
def edit_creator_form(creator_id):

    form = CreatorForm()
    creator = Creators.query.filter_by(id = creator_id).first()

    form.first_name.data = creator.first_name
    form.last_name.data = creator.last_name
    form.nick_name.data = creator.nick_name
    form.url_picture.data = creator.url_picture
    form.email.data = creator.email
    form.topics.data = creator.topics
    form.instagram.data = creator.instagram
    form.tik_tok.data = creator.tik_tok
    form.facebook.data = creator.facebook
    form.twitter.data = creator.twitter
    form.youtube.data = creator.youtube
    form.total_followers.data = creator.total_followers

    return render_template('forms/edit-creator.html', form=form, creator=creator)


@app.route('/creator/<int:creator_id>/edit', methods= ['POST'])
#@requires_auth('patch:creator-profile')
def edit_creator_submission(creator_id):

    error = False
    form = CreatorForm()
    
    try:
    
        first_name = form.first_name.data
        last_name = form.last_name.data
        nick_name = form.nick_name.data
        url_picture = form.url_picture.data
        email = form.email.data
        topics = form.topics.data
        instagram = form.instagram.data
        tik_tok = form.tik_tok.data
        facebook = form.facebook.data
        twitter = form.twitter.data
        youtube = form.youtube.data
        total_followers = form.total_followers.data

     
        creator=update(Creators).where(Creators.id == creator_id).values(first_name = first_name, last_name = last_name, nick_name = nick_name, url_picture = url_picture, email = email, topics = topics,
        instagram = instagram, tik_tok = tik_tok, facebook = facebook, twitter = twitter, youtube = youtube, total_followers = total_followers)
        
        db.session.execute(creator)
        db.session.commit()

    except:
        
        db.session.rollback()
        error = True
        

    finally:
        db.session.close()

    if error:
        abort(500)
     
    
    return redirect(url_for('show_profile', creator_id=creator_id))
    



#------------------------------------#
# Publishers routes
#------------------------------------#


@app.route('/publishers-profile/<int:publisher_id>', methods=['GET'])
#@requires_auth('get:publisher-profile')
def view_publisher_profile(publisher_id):

    publisher_profile = Publisher.query.get_or_404(publisher_id)
    campaigns_created = Campaigns.query.filter_by(id_publisher = publisher_id).count()


    return render_template('home/publishers-profile.html', profile=publisher_profile, campaigns = campaigns_created, status_code=200)

#------------------------------------------#
#Campigns routes
#-------------------------------------------#


# Publishers could only see their own campaigns. This route is used for creators too and can only see theirs

@app.route('/campaigns', methods=['GET'])
#@requires_auth('get:campaigns')
def list_campaigns():

   campaign = Campaigns.query.all()
   
   return render_template('home/campaigns.html', campaing=campaign)



@app.route('/campaigns/new', methods=['GET'])
#@requires_auth('get:campaigns')
def new_campaign_form():

    error = False
    form = CampaignForm()

    creators = Creators.query.all()

    return render_template('forms/new-campaign.html', form=form, creators = creators) 

@app.route('/campaigns/new', methods=['POST'])
#@requires_auth('post:campaigns')
def new_campaign_submit():

    error = False
    form = CampaignForm()

    try: 
        name = form.name.data
        start_date = form.start_date.data
        last_date = form.last_date.data
        budget = form.budget.data
        sources = form.sources.data
        description = form.description.data
        creator = form.creator.data
    
        campaign = Campaigns(name = name, start_date = start_date, last_date = last_date, budget = budget, sources = sources, description = description, creator = creator)
        
        db.session.add(campaign)
        flash('Campaign ' + form.name.data + ' was successfully listed!')
        db.session.commit()
  
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()
    
    return redirect(url_for('list_campaigns'))    

@app.route('/campaigns/<int:campaign_id>/delete', methods=['GET', 'DELETE'])
#@requires_auth('delete:campaigns')
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

    return redirect(url_for('campaigns'))
       

#Error handlers

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.errorhandler(400)
def forbidden_error(error):
    return render_template('home/page-400.html'), 400

@app.errorhandler(401)
def server_error(error):
    return render_template('home/page-401.html'), 401

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('home/page-403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('home/page-500.html'), 500

@app.route('/headers')
@requires_auth('get:creators')
def headers(payload):
    print(payload)
    return 'Access Granted'

# Default port and launch

if __name__ == "__main__":
    app.run(debug=True, port=8080)

