from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
import re

class CreatorForm(Form):
    first_name = StringField(
        'name', validators=[DataRequired()]
    )
    last_name = StringField(
        'last_name', validators=[DataRequired()]
    )
    nick_name = StringField(
        'nick', validators=[DataRequired()]
    )
    email = StringField(
        'email', validators=[DataRequired()],
        
    )
    topics = StringField(
        
        'topics', validators=[DataRequired()],
    )
    url_picture = StringField(
        'url_picture', validators=[DataRequired()],
    )
   
    instagram= StringField(
        'instagram', validators=[DataRequired()]
     )

    tik_tok = StringField(
        'tik_tok', validators=[DataRequired()]
     )

    facebook = StringField(
        'facebook', validators=[DataRequired()]
     )
    twitter = StringField(
        'twitter', validators=[DataRequired()]
     )
    youtube = StringField(
        'youtube', validators=[DataRequired()]
     )
    total_followers = StringField(
        'followers', validators=[DataRequired()]
     )
   
class PublisherForm(Form):

    name = StringField(
        'name', validators=[DataRequired()]
    )
    description = StringField(
        'description', validators=[DataRequired()]
    )
    industry = StringField(
        'industry', validators=[DataRequired()]
    )
    email = StringField(
        'email', validators=[DataRequired()],
        
    )
    url_logo = StringField(
        'logo', validators=[DataRequired()],
    )
   
    website= StringField(
        'website', validators=[DataRequired()]
     )


class CampaignForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    start_date = DateTimeField(
        'start',
        validators=[DataRequired()],
        default= datetime.today()
    )
    last_date = DateTimeField(
        'last',
        validators=[DataRequired()],
        default= datetime.today()
    )
    budget = StringField(
        'budget', validators=[DataRequired()]
    )
    sources = StringField(
        'sources', validators=[DataRequired()]
    )
    description= StringField(
        'description', validators=[DataRequired()]
    )
    creator = SelectMultipleField(
        'creator', 
    )

