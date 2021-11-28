import mysql.connector
from mysql.connector import errorcode
from Credentials import constants
from datetime import date

def init_connection_sql():
    # Initialise connection for MySQL
    return mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD
                                   )

'''
readMapDataFromDB
    Reads the map level file path from the database 
        @param mid  Refers to the map ID to fetch the the DB
        @return pw[0]   The map level file path
        @return pw[1]   The map name
'''
def readMapDataFromDB(mid):
    conn = init_connection_sql()
    cur = conn.cursor()
    query = ("select * from levels where map_id = %s")
    cur.execute(query, (mid,))

    pw = cur.fetchone()

    # close connection
    cur.close()
    conn.close()

    return pw[0], pw[1], pw[2], pw[3]


'''
storeGameDataToDB
    Stores the game data to the database 
        @param mid  Refers to the map ID to fetch the the DB
        @return pw[0]   The map level file path
        @return pw[1]   The map name
'''
def storeGameDataToDB(map_id, map_difficulty, dist_travelled, game_duration):
    conn = init_connection_sql()
    cur = conn.cursor(prepared=True)

    game_date = date.today().strftime("%Y-%m-%d")

    cur.execute("""INSERT INTO coolmotor.dashboard (date, game_duration, map_id, map_difficulty, distance_travelled) 
        VALUES (%s, %s, %s, %s, %s);""", (game_date, game_duration, map_id, map_difficulty, dist_travelled))
    conn.commit()
    cur.close()
    conn.close()
    return "Insert Level success"



'''
initLevelLayout
    Reads the map data from the text file, parses the map data into JSON format.
        @param mapFile  The map level file path
        @param mapLevelLayout  The map level details in JSON
        @param commandList  The full command list
        
        @return commandList  The parsed command list according to the map text file specs.
        @return mapLevelLayout  The map level details in JSON
'''
def initLevelLayout(mapFile):

    # our map level json object
    mapLevelLayout = {"rows":5, "cols":5, "tsize":512, "tiles":[]}
    commandList = ["upward", "downward", "left", "right", "loop"]

    with open(mapFile, "r") as f:

        # i is counter
        i = 1
        for line in f.readlines():

            # create blockly commands to display later
            if i == 1:

                # loop through commandList, blank out the blocks that are disabled.
                # the range is len(line) - 1 to account for newline character.
                for x in range(len(line) - 1):
                    if int(line[x]) == 0:
                        commandList[x] = ""
                # increase counter so we dont ever come in here again
                i += 1

            else:
                # create map tiles to display later
                for x in line:
                    if x != '\n':
                        mapLevelLayout.get("tiles").append(x)

    return commandList, mapLevelLayout