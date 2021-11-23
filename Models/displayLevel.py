import mysql
from mysql.connector import errorcode
from Credentials import constants




'''
this function gets all the data stored in the Level table. 
'''
# to display level history saved in database
def display():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor(prepared=True)
    query = "SELECT * FROM levels;"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


'''
delete() function takes in a variable which should be the map_id for the
levels table. it deletes that row on the table. 
    @param x        the map_id that determines the row to be deleted
'''
def delete(map_id):
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    x = int(map_id)
    cur = conn.cursor(prepared=True)
    cur.execute("DELETE FROM levels WHERE map_id = %s;", (x,))
    conn.commit()
    cur.close()
    conn.close()
