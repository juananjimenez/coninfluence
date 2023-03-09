CONFLUENCE.IO Final Capstone project for Fullstack Nanodegree. Udacity program.

Base URL
https://

Motivations
This projects simulates a Digital Agency where Publishers can contact content creators and assign social media campaigns to them. The app was designed using ARGON dashboard template. 

Getting Started
Installing Dependencies
Python 3.10
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to directory and running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Database Setup
for my local postgres path :"postgres://{}:{}@{}/{}".format( 'student', 'student', 'localhost:5432', coninfluence" for my postgres in Render
this is the postgress url


Running the server
From within the starter directory first ensure you are working using your created virtual environment.

To run the server (localhost:8080), execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run 

TASKS

The full dashboard after login shows a menu with three options with authorization requirements dependending if your role is Publisher o Creator 

Use Flask-CORS to enable cross-domain requests and set response headers.

Create an endpoint to handle GET requests for creators list
Create an endpoint to handle GET requests for campaigns list
Create an endpoint to handle GET requests for user profile information
Create an endpoint to DELETE campaigns.
Create an endpoint to UPDATE creators profile by id (Only the own creator could modify his or her profile)
Create an endpoint to UPDATE publishers profile (Only the own publisher could modify his profile)
Create an endpoint to CREATE new campaigns (Only the publisher could do it)
Create error handlers for all expected errors including 400, 401, 403, 404, and 500.

AUTH0
The application for this api is Coninfluence80 and the API name is coninfluence.

There are actually to roles: creators and publishers. Creators only can access their profile and see the campaigns in which they are enroled. Publishers has all permissions except create and update creators profile.

Publisher permissions: delete:campaigns, get:campaigns, get:creators, get:publisher-profile, post:campaign, post:publisher-profile, update:campaigns, update:profile

Creators permissions: get:creators-profile, post:creator-profile
Test your endpoints with Postman.
You've got two users for test purposes:
rosa.diez@nike.com (publisher). Pass: rosa.diez.nike.1. Permissions: [delete:campaigns], [get:campaigns], [get:creators], [get:creators-profile], [get:publisher-profile], [post:campaign], [post:creator-profile], [post:publisher-profile],[update:campaigns], [update:profile]

cristina.cifuentes@pp.es (creator). Pass: cristina.cifuentes.pp.1 Permissions: [get:creators-profile], [post:creator-profile]

END POINTS

GET ('/login') Entry point that redirects to Auth0 login page

GET ('/') After login this is the callback where you are redirected and see your dashboard.


GET (/profile/<int:creator_id>) Requires permission: get:profile: 

{ "profile": [ { "first_name": "Carlos", "last_name": "Orellana", "nick_name": "Carlitos", "url_picture": "https://carlitos.jpg", "email": "carlitos@gmail.com", "topics": "Fifa, Xbox, King of Leyends", "instragram": None, "tik_tok": None, "facebook": None, "Twitter": None, "youtube": "www.youtube.com/carlitos", "total_followers": 2345678}] 

GET (/creators) Requires permission: get:creators:

{"creators": [{"nick_name": "carlitos", "total_followers": 234567, "topics": "Fifa, Xbox, King of Leyends", "channels": "youtube" }]}

GET (/creators/new) Requires permission: get:creator-profile:
{
first_name,
last_name,
nick_name,
url_picture,
email,
topics,
instagram,
tik_tok,
facebook,
twitter,
youtube,
total_followers,
}

POST (/creators/new) permission: post:creator-profile:

{
"first_name": "Carlos",
"last_name": "Orellana",
"nick_name": "Carlitos",
"url_picture": "https://carlitos.jpg",
"email": "carlitos@gmail.com",
"topics": "Fifa, Xbox, King of Leyends",
"instagram": None,
"tik_tok": None,
"facebook": None,
"twitter": None,
"youtube", "youtube.com/carlitos",
"total_followers", 345678
}

GET (/creator/<int:creator_id>/edit) permission: get:creator-profile:

{
"first_name": "Carlos",
"last_name": "Orellana",
"nick_name": "Carlitos",
"url_picture": "https://carlitos.jpg",
"email": "carlitos@gmail.com",
"topics": "Fifa, Xbox, King of Leyends",
"instagram": None,
"tik_tok": None,
"facebook": None,
"twitter": None,
"youtube", "youtube.com/carlitos",
"total_followers", 345678
}

POST (/creator/<int:creator_id>/edit) permission: post:creator-profile. This endpoint doesn't works with PUT

{
"first_name": "Carlos",
"last_name": "Orellana",
"nick_name": "Carlitos",
"url_picture": "https://carlitos.jpg",
"email": "carlitos@gmail.com",
"topics": "Fifa, Xbox, King of Leyends",
"instagram": None,
"tik_tok": None,
"facebook": None,
"twitter": None,
"youtube", "youtube.com/carlitos",
"total_followers", 345678
}


GET ('/publishers-profile/<int:publisher_id>') Requires permission: get:publisher-profile

{
"company_name": "Nike",
"email": "rosa.diez@nike.com",
"industry": "sportswear",
"website": "www.nike.com",
"url_logo": "http://nike.com/logo.jpg,
"twitter": None,
"campaigns_launched", 1

}

GET ('/campaigns') Requires permission: get:campaigns

{
"name": "Leo Messi soccer boots promotion",
"start_date": 2023-07-20 00:00:00
"last_date": 2023-10-23 00:00:00
"budget": "50000 $"
"creator": None
}

POST ('/campaigns/new') Requires permission: post:campaigns':

{
"name": "Leo Messi soccer boots promotion",
"start_date": 2023-07-20 00:00:00
"last_date": 2023-10-23 00:00:00
"budget": "50000 $"
"creator": None,
"description": "Launche Leo Messi new boots",
"sources": "youtube.com",
}

DELETE ('/campaigns/<int:campaign_id>/delete') Requires permission: delete:campaigns


UNIT TEST
to run test cases use this command $ python test.py. It's configured for all the endpoints.

