# from Models import EditLevel
from Models.EditLevel import fetchPassword, insert_Level
import unittest

class TestEditLevel(unittest.TestCase):
    
    def test_fetchPassword(self):
        pw = []
        result = fetchPassword()
        for i in result:
            pw.append(i[0])
            res = i[0]
        self.assertEqual(res, 'admin')
        
    # def test_init_connection_sql(self):
    
    def test_insert_Level(self):
        result = insert_Level(2, "shawn5", 'Levels/66.txt')
        print(result)
        self.assertEqual(result, "Insert Level success")
        
    # def test_fetch_LastMapID(self):
    #     result = fetch_LastMapID()
    #     self.assertIs(result, 50)
        
if __name__ == '__main__':
    unittest.main()




# import requests
# import pytest
# import sqlite3
# from CoolMotor import app as flask_app

# @pytest.fixture
# def setup_database():
#     """ Fixture to set up the in-memory database with test data """
#     conn = sqlite3.connect(':memory:')
#     cursor = conn.cursor()
#     cursor.execute('''
# 	    CREATE TABLE accounts
#         (user_id integer, pw text)''')
#     cursor.execute('''
# 	    CREATE TABLE levels
#         (map_id integer, map_difficulty integer, map_name text, map_level_layout text)''')
#     sample_data1 = [
#         (0, 'admin')
#     ]
#     sample_data2 = [
#         (1, 1, 'China', 'Levels/1.txt')
#     ]
#     cursor.executemany('INSERT INTO accounts VALUES(?, ?)', sample_data1)
#     cursor.executemany('INSERT INTO levels VALUES(?, ?, ?, ?)', sample_data2)
    
#     yield conn

# def test_fetchPassword(setup_database):
#     cursor = setup_database
#     data = cursor.execute('SELECT * FROM accounts').fetchall()
#     # print('test')
#     # print(data)
#     for i in data:
#         pw = i[1]
#     # print(pw)
#     assert pw == 'admin'



# def test_insert_Level(setup_database):
#     cursor = setup_database
#     data = cursor.execute('SELECT * FROM levels').fetchall()
#     print(data)