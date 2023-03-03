import unittest
import json
from app import app
from models import db, Publisher, Campaigns, Creators
import os
from dotenv import load_dotenv


load_dotenv()


class ConinfluenceTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.database_name = "coninfluence_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format("student", "student", "localhost:5432", self.database_name)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = self.database_path


        with self.app.app_context():
            self.db = db
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_home(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
       
    def test_list_creators(self):
        res = self.client().get('/creators')
        self.assertEqual(res.status_code, 200)

    def test_profile(self):
        res = self.client().get('/profile/3')
        self.assertEqual(res.status_code, 200)
    
    def test_new_creator_get(self):
        res=self.client().get('/creators/new')
        self.assertEqual(res.status_code, 200)
        
    def test_new_creator_post(self):
        res=self.client().post('/creators/new')
        self.assertEqual(res.status_code, 200)

    def test_creator_edit_get(self):
        res=self.client().get('/creator/3/edit')
        self.assertEqual(res.status_code, 200)

    def test_creator_edit_post(self):
        

    # @app.route('/creator/<int:creator_id>/edit', methods= ['GET'])

    # @app.route('/creator/<int:creator_id>/edit', methods= ['POST'])

    # @app.route('/publishers-profile/<int:publisher_id>', methods=['GET'])

    # @app.route('/campaigns', methods=['GET'])

    # @app.route('/campaigns/new', methods=['GET'])

    # @app.route('/campaigns/new', methods=['POST'])

    # @app.route('/campaigns/<int:campaign_id>/delete', methods=['GET', 'DELETE'])


if __name__ == "__main__":
    unittest.main()

