import mysql.connector
from mysql.connector import errorcode
from Credentials import constants


def readMapDataFromDB(mid):
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)

    cur = conn.cursor()
    query = ("select map_level_layout from levels where map_id = %s")
    cur.execute(query, (mid,))

    pw = cur.fetchone()

    # close connection
    cur.close()
    conn.close()

    return pw[0]


def initLevelLayout(mapFile):

    with open(mapFile, "r") as f:

        # i is counter
        i = 1
        for line in f.readlines():

            if i == 1:
                # render blockly
                i += 1
                pass

            else:
                # render map
                print(line)