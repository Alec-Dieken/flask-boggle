from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn('game-container', session)
            self.assertIn(b'Points:', response.data)
            self.assertIn(b'Timer:', response.data)

    def test_valid_word(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["D", "A", "Y", "H", "Z"], 
                                 ["X", "O", "O", "L", "V"], 
                                 ["H", "V", "G", "T", "R"], 
                                 ["U", "E", "E", "E", "K"], 
                                 ["J", "B", "Q", "G", "F"]]
        response = self.client.post('/handle', {'guess': 'dog'})
        self.assertEqual(response.json['answer'], 'ok')

    def test_invalid_word(self):
        self.client.get('/')
        response = self.client.post('/handle', {'guess': 'impossible'})
        self.assertEqual(response.json['answer'], 'not-on-board')

    def not_a_word(self):
        self.client.get('/')
        response = self.client.post('/handle', {'guess': 'dfgsrgftghfht'})
        self.assertEqual(response.json['answer'], 'not-word')