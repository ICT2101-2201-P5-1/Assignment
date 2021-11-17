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

    # our map level json object
    mapLevelLayout = {"row":5, "col":5, "tiles":[]}
    commandList = ["upward", "downward", "left", "right", "loop", "if_wall", "if_coin"]

    with open(mapFile, "r") as f:

        # i is counter
        i = 1
        for line in f.readlines():

            # render blockly commands
            if i == 1:

                # loop through commandList, blank out the blocks that are disabled.
                # the range is len(line) - 1 to account for newline character.
                for x in range(len(line) - 1):
                    if int(line[x]) == 0:
                        commandList[x] = ""
                # increase counter so we dont ever come in here again
                i += 1

            else:
                # render map
                print(line)

    return commandList, None