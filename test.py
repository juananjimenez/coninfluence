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
        app.config['SQLALCHEMY_DATABASE_URI_TEST'] = self.database_path


        with self.app.app_context():
            self.db = db
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_home(self):
        res = self.client().get('/')
        #self.assertEqual(res.status_code, 200)
       
    def test_list_creators(self):
        res = self.client().get('/creators')
        #self.assertEqual(res.status_code, 200)

    def test_profile(self):
        res = self.client().get('/profile/2')
        #self.assertEqual(res.status_code, 200)
    
    def test_new_creator_get(self):
        res=self.client().get('/creators/new')
        #self.assertEqual(res.status_code, 200)
        
    def test_new_creator_post(self):
        res=self.client().post('/creators/new')
        #self.assertEqual(res.status_code, 200)

    def test_creator_edit_get(self):
        res=self.client().get('/creator/6/edit')
        #self.assertEqual(res.status_code, 200)

    def test_creator_edit_post(self):
        res=self.client().post('/creator/6/edit')
        #self.assertEqual(res.status.code, 200)

    def test_publishers_get(self):
        res=self.client().get('/publishers-profile/2')
        #self.assertEqual(res.status.code, 200)

    def test_campaigns_get(self):
        res=self.client().get('/campaigns')
        #self.assertEqual(res.status.code, 200)

    def test_campaigns_new_get(self):
        res=self.client().get('/campaigns/new')
        #self.assertEqual(res.status.code, 200)

    def test_campaigns_new_post(self):
        json_campaigns = {
            'name': 'H&M',
            'start_date': '2023-01-01',
            'last_date': '2023-02-01',
            'budget': '2000',
            'sources': 'Facebook',
            'description': 'For test',
            'id_creator': '3',
            'id_publisher': '6'

        }
        res=self.client().post('/campaigns/new', json = json_campaigns)
        data = json.loads(res.data)
        #self.assertEqual(res.status.code, 200)
        self.assertEqual(data['success'], True)
    
    def test_campaigns__delete_get(self):
        res=self.client().get('/campaigns/2/delete')
        #self.assertEqual(res.status.code, 200)
    
    def test_campaigns_delete_delete(self):
        res=self.client().delete('/campaigns/2/delete')
        #self.assertEqual(res.status.code, 200)


if __name__ == "__main__":
    unittest.main()

