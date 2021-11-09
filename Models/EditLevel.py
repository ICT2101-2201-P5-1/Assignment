import mysql.connector
from mysql.connector import errorcode
from Credentials import constants


def fetchPassword():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT pw FROM accounts;")
    cur.execute(query)
    pw = cur.fetchall()
    cur.close()
    conn.close()
    return pw