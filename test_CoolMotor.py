import unittest
import CoolMotor
import json
from CoolMotor import app
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response,session


class TestCoolMotor(unittest.TestCase):
    """
    White box testing code for code in displayLevel.py
    , edit_level(), view_display_Level()
    and def delete_level(id) in CoolMotor.py
    """

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_edit_level(self):
        rv = self.client.get('/edit_level')
        assert rv.status_code == 200
        assert b'<h2 class="map-title"> Edit Map </h2>' in rv.data

    def test_edit_level2(self):
        x= {"position":"22","type":"goal"}
        values=json.dumps(x)
        rv = self.client.post('/edit_level', data={'javascript_data':values})
        self.assertEqual(rv.status_code, 200)
        assert b'<h2 class="map-title"> Edit Map </h2>' in rv.data

    def test_view_display_Level(self):
        rv = self.client.get('/displayLevel')
        assert rv.status_code == 200
        assert b'<th>Map ID</th>' in rv.data

    def test_delete_level(self):
        rv = self.client.post('/deletelevel/5')
        assert rv.status_code == 302
        assert b' redirected automatically to target URL: <a href="/displayLevel">/displayLevel</a>' in rv.data

if __name__ == '__main__':
    unittest.main()