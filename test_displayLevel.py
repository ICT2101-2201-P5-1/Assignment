import pytest
import CoolMotor
import sqlite3
import requests
from CoolMotor import app as flask_app

@pytest.fixture
def setup_database():
    """Fixture to setup database in memory"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE levels
                    (map_id integer, map_difficulty integer, map_name text, map_level_layout text) 
                    ''')
    sample_data = [
        ('1', '1', 'map', 'map'), ('2', '2', 'map', 'map'),
    ]
    cursor.executemany('INSERT INTO levels VALUES (?, ?, ?, ?)', sample_data)
    yield conn


def test_display(setup_database):
    cur = setup_database
    query = "SELECT * FROM levels;"
    cur.execute(query)
    data = cur
    cur.close()
    assert data != 0


def test_delete(setup_database):
    x = 1
    cur = setup_database
    cur.execute("DELETE FROM levels WHERE map_id = %s;", (x,))
    cur.execute("select from levels wheremap_id =%s;", (x,))
    data = cur
    cur.close()
    assert data == ''
