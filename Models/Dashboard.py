import mysql.connector
from mysql.connector import errorcode
from Credentials import constants

# Hi Friends and Professors! Shawn(2001401) here. These controllers are for the dashboard!



# This fetches the data to be displayed in the table at dashboard.html
def fetchData():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT * FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

# These 2 fetches data to be converted into the first chart at CoolMotor.py
def fetchChart1y():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT distance_travelled FROM dashboard;")
    cur.execute(query)
    data1x = cur.fetchall()
    cur.close()
    conn.close()
    return data1x

def fetchChart1x():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT entry_id FROM dashboard;")
    cur.execute(query)
    data1y = cur.fetchall()
    cur.close()
    conn.close()
    return data1y

# These 2 fetches data to be converted into the second chart at CoolMotor.py
def fetchChart2y():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT game_duration FROM dashboard;")
    cur.execute(query)
    data1x = cur.fetchall()
    cur.close()
    conn.close()
    return data1x

def fetchChart2x():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT date FROM dashboard;")
    cur.execute(query)
    data1y = cur.fetchall()
    cur.close()
    conn.close()
    return data1y


# Thanks!