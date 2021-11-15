import mysql.connector
from mysql.connector import errorcode
from Credentials import constants


def init_connection_sql():
    '''
    Initialise connection for MySQL
    '''
    return mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD
                                   )


def fetchPassword(): 
    conn = init_connection_sql()
    cur = conn.cursor()
    query = ("""SELECT pw FROM accounts;""")
    cur.execute(query)
    pw = cur.fetchall()
    cur.close()
    conn.close()
    return pw


def insert_Level(Difficulty, LevelName, fileName):
    conn = init_connection_sql()
    cur = conn.cursor()
    cur.execute("""INSERT INTO cool_motor.levels ( map_difficulty, map_name, map_level_layout) 
    VALUES ( %s, %s, %s);""",(Difficulty, LevelName, fileName))
    conn.commit()
    cur.close()
    return "Insert Level success"