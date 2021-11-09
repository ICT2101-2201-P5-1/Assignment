import mysql.connector
from mysql.connector import errorcode


def test(query):
    cnx = mysql.connector.connect(user='cooladmin', password='2101motor',
                                    host='database-1.cbuwe4uyyt2j.ap-southeast-1.rds.amazonaws.com',
                                    database='cool_motor')
    cursor = cnx.cursor()
    cursor.execute(query)
    for (pw) in cursor:
        print("{}".format(pw))