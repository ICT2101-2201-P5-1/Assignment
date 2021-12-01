import unittest
import CoolMotor
from CoolMotor import app
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response,session
'''
White box testing code for code in displayLevel.py 
and edit_level(), 
view_display_Level() 
and def delete_level(id) in CoolMotor.py by Tudy 
'''
'''
@app.route("/deletelevel/<int:id>", methods=['POST'])
def delete_level(id):
    Models.displayLevel.delete(id)
    session.pop('_flashes', None)
    flash('Deletion Successful', "info")
    return redirect(url_for('view_display_Level'))


'''


class TestCoolMotor(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_edit_level(self):
        rv = self.app.get('/edit_level')
        assert rv.status_code == 200
        assert b'<h2 class="map-title"> Edit Map </h2>' in rv.data

    def test_view_display_Level(self):
        rv = self.app.get('/displayLevel')
        assert rv.status_code == 200
        assert b'<th>Map ID</th>' in rv.data

    def test_delete_level(self):
        rv = self.app.post('/deletelevel/5')
        assert rv.status_code == 302
        assert b' redirected automatically to target URL: <a href="/displayLevel">/displayLevel</a>' in rv.data
