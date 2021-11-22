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

'''
Insert Level details into coolmotor.levels
    @param Difficulty value 1(easy),2(medium),3(hard)
    @param LevelName String levelName user input
    @param fileName is path to generated textfile
    @return "Insert Level success" notify user

''' 
def insert_Level(Difficulty, LevelName, fileName):
    conn = init_connection_sql()
    cur = conn.cursor()
    cur.execute("""INSERT INTO coolmotor.levels ( map_difficulty, map_name, map_level_layout) 
    VALUES ( %s, %s, %s);""",(Difficulty, LevelName, fileName))
    conn.commit()
    cur.close()
    conn.close()
    return "Insert Level success"

'''
Get the last MapID inserted into database
    
''' 
def fetch_LastMapID():
    conn = init_connection_sql()
    cur = conn.cursor()
    query = """SELECT map_id 
        FROM coolmotor.levels
        ORDER BY map_id DESC;"""
    cur.execute(query)
    MapIDList = cur.fetchall()
    MapIDTuple = MapIDList[0]
    LastMapID = int(MapIDTuple[0])
    print(LastMapID)
    cur.close()
    conn.close()
    return LastMapID
