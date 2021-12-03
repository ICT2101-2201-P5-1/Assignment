import mysql
from mysql.connector import errorcode
from Credentials import constants


# to display level history saved in database
def display():
    """
    This function gets all the data stored in the Level table.
    """
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = "SELECT * FROM levels;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def delete(map_id):
    """
    delete() function takes in a variable which should be the map_id for the
    levels table. it deletes that row on the table.
        @param x        the map_id that determines the row to be deleted
    """
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    x = int(map_id)
    cur = conn.cursor()
    cur.execute("DELETE FROM levels WHERE map_id = %s;", (x,))
    conn.commit()
    cur.close()
    conn.close()
    return "Delete Successful"
