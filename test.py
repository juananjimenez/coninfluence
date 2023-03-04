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

       
    def test_list_creators(self):
        res = self.client().get('/creators')
 

    def test_profile(self):
        res = self.client().get('/profile/2')
 
    
    def test_new_creator_get(self):
        res=self.client().get('/creators/new')
  
        
    def test_new_creator_post(self):
        
        json_creator = {
            'first_name': 'Ruphert',
            'last_name': 'Everet',
            'nick_name': 'LionKing',
            'url_picture': 'https://blog.hubspot.com/hubfs/top-instagram-influencers.jpg',
            'email': 'lionking@gmail.com',
            'topics': 'Sports',
            'instagram': '@lionking',
            'twitter': '@lionking',
            'tik_tok': '@lionking',
            'facebook': '@lionking',
            'youtube': '@lionking',
            'total_followers': '13000',
        }
        res=self.client().post('/creators/new', json = json_creator)
       

    def test_creator_edit_get(self):
        res=self.client().get('/creator/6/edit')
        

    def test_creator_edit_patch(self):

        json_creator_update = {
            'first_name': 'Ruphert',
            'last_name': 'Everet',
            'nick_name': 'LionKing',
            'url_picture': 'https://blog.hubspot.com/hubfs/top-instagram-influencers.jpg',
            'email': 'lionking@gmail.com',
            'topics': 'Sports',
            'instagram': '@lionking',
            'twitter': '@lionking',
            'tik_tok': '@lionking',
            'facebook': '@lionking',
            'youtube': '@lionking',
            'total_followers': '13000',
        }
        res=self.client().patch('/creator/6/edit', json = json_creator_update)
       

    def test_publishers_get(self):
        res=self.client().get('/publishers-profile/2')
      

    def test_campaigns_get(self):
        res=self.client().get('/campaigns')
      

    def test_campaigns_new_get(self):
        res=self.client().get('/campaigns/new')
   

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
       
    
    def test_campaigns__delete_get(self):
        res=self.client().get('/campaigns/2/delete')
  
    
    def test_campaigns_delete_delete(self):
        res=self.client().delete('/campaigns/2/delete')
  

    def test_404_profile(self):
        res = self.client().get('/profile/<int:creator_id>', json={'id': 1000})
        self.assertEqual(res.status_code, 404)
        


if __name__ == "__main__":
    unittest.main()

