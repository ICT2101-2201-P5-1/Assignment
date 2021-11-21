import mysql.connector
from mysql.connector import errorcode
from Credentials import constants


def readMapDataFromDB(mid):
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)

    cur = conn.cursor(prepared=True)
    query = ("select map_level_layout from levels where map_id = %s")
    cur.execute(query, (mid,))

    pw = cur.fetchone()

    # close connection
    cur.close()
    conn.close()

    return pw[0]


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