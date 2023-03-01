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
            #self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # def test_list_creators(self):
    #     res = self.client().get('/creators')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data('success', True))
        
   

if __name__ == "__main__":
    unittest.main()