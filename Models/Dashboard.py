import mysql.connector
from mysql.connector import errorcode
from Credentials import constants

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