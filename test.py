import unittest
import json
from app import app
from models import db, Publisher, Campaigns, Creators
from config import SQLALCHEMY_DATABASE_URI_TEST
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


class ConinfluenceTest(unittest.TestCase):

    def setUp(self):
        
        self.database_name = "coninfluence_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format("test", "test", "localhost:5432", self.database_name)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI_TEST'] = self.database_path
        db.init_app(app)
        

        self.new_creator = {
            'first_name': 'Robert', 
            'last_name': 'Smith', 
            'nick_name': 'Alterior',
            'url_picture': 'https://blog.hubspot.com/hubfs/top-instagram-influencers.jpg',
            'email': 'alterior@gmail.com',
            'topics': 'soccer, toros',
            'instragram': '@alterior',
            'tik_tok': '@alterior',
            'twitter': '@alterior',
            'youtube': 'www.youtube.com/alterior',
            'total_followers': '678000',
        }

        self.new_publisher = {
            'name': 'Reebok', 
            'description': 'Sportswear company', 
            'industry': 'Sportswear',
            'website': 'https://www.reebok.com',
            'email': 'reebok@gmail.com',
            'url_logo': 'https://blog.hubspot.com/hubfs/top-instagram-influencers.jpg',
        }

        self.new_campaign = {
            'name': 'Nadal t-shirt', 
            'start_date': '2023-01-01', 
            'last_date': '2023-02-01',
            'budget': '50000',
            'sources': 'instagram, twitter',
            'description': 'Promote new Rafa Nadal t-shirt',
        }

        with app.app_context():
            db.create_all()

    def tearDown(self):
        pass

    def test_get_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    # def test_404_sent_requesting_valid_page(self):
    #     res = self.client().get('/books?page=1000', json={'rating': 1})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "Not found")

    # def test_book_search_with_results(self):
    #     res = self.client().post('/books', json={'search':'novel'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['Total books'])
    #     self.assertEqual(len(data['books']), 4)

    # def test_book_search_without_results(self):
    #     res = self.client().post('/books', json={'search':'applejacks'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['Total books'], 0)
    #     self.assertEqual(len(data['books']), 0)

if __name__ == "__main__":
    unittest.main()