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

END POINTS
GET /actors Request Headers: None Requires permission: read:actors Using Postman with sample below and curl Sample: curl -X GET https://abdelrahmanproj.herokuapp.com/actors

{ "actors": [ { "age": 30, "gender": "male", "id": 1, "name": "Mohamed" } ], "success": true } 

GET /movies Request Headers: None Requires permission: read:movies Using Postman with sample below Sample: curl -X GET https://abdelrahmanproj.herokuapp.com/movies

{ "movies": [ { "id": 1, "release_date": "Mon, 12 Oct 2020 00:00:00 GMT", "title": "comedy" } ], "success": true }

DELETE /actors/actor_id Request Arguments: integer id Request Headers: None Requires permission: delete:actors Using Postman with sample below Sample: curl -X DELETE https://abdelrahmanproj.herokuapp.com/actors/2

{
"deleted": 2,
"success": true
}

DELETE /movies/movie_id Request Arguments: integer id Request Headers: None Requires permission: delete:movies Using Postman with sample below Sample: curl -X DELETE https://abdelrahmanproj.herokuapp.com/actors/1

{ "deleted": 1, "success": true }

POST /actors Request Arguments: None Request Headers: (application/json) string name - integer age - string gender Requires permission: create:actors Using Postman with sample below Sample: curl -X POST https://abdelrahmanproj.herokuapp.com/actors

{
"actor_id": 3,
"actors": {
    "age": 22,
    "gender": "female",
    "name": "Mary"
},
"success": true
}

POST /movies Request Arguments: None Request Headers: (application/json) string title - date release_date Requires permission: create:movies Using Postman with sample below Sample: curl -X POST https://abdelrahmanproj.herokuapp.com/movies

{
"movie_id": 1,
"movies": {
    "release_date": "2020-10-12",
    "title ": "comedy"
},
"success": true
}

PATCH /actors/actor_id Request Arguments: integer id Request Headers: (application/json) string name - integer age - string gender Requires permission: edit:actors Using Postman with sample below Sample: curl -X PATCH https://abdelrahmanproj.herokuapp.com/actors/3

{
"actor": [
    {
        "age": 27,
        "gender": "female",
        "id": 3,
        "name": "Mary"
    }
],
"success": true,
"updated": 3
} PATCH /movies/movie_id Request Arguments: integer id Request Headers: (application/json) string title - date release_date Requires permission: edit:movies Using Postman with sample below Sample: curl -X PATCH https://abdelrahmanproj.herokuapp.com/movies/1

{
"movie": [
    {
        "id": 1,
        "release_date": "Mon, 12 Oct 2020 00:00:00 GMT",
        "title": "action"
    }
],
"success": true,
"updated": 1
}

UNIT TEST
to run test cases use this command $ python test.py. It's configured for all the endpoints.

