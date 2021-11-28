import pytest
import CoolMotor
from CoolMotor import app as flask_app

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



@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_edit_level(app,client):
    res = client.get('/edit_level')
    assert res.status_code == 200
    html = res.data.decode()
    assert "<h3>Drag Item to map:</h3>" in html
    assert "<form name=\"Level_Editor_Form\" method=\"POST\" action=\"/getMAPData\">" in html
    assert "<h2 class=\"map-title Commands2\"> Save Level </h2>" in html


def test_view_display_level(app,client):
    res = client.get('/displayLevel')
    assert res.status_code == 200
    html = res.data.decode()
    assert "<th>Map ID</th>" in html
    assert "<th>Map Difficulty</th>" in html
    assert "<th>Map Name</th>" in html
    assert "<th>Delete</th>" in html


