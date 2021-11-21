import mysql.connector
from Credentials import constants

'''
fetchData() function is to fetch the data from the dashboard table in the coolmotor database
    @param conn               Opens the connection with the database
    @param cur                Initialise the cursor which accesses the databse
    @param query              Initialises the SQL qeury
    @param cur.execute(query) Executes an sql query with the data stored in the query parameter
    @param data               Stores the data from the query
    @param cur.close()        Closes the access to the database
    @param conn.close()       Closes the connection to the database
    @return                   Returns the data that is fetched
'''
def fetchData():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT * FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

'''
fetchChart1y() function is to fetch the data from the dashboard table in the coolmotor database
to be used in the y axis of the 1st chart
    @param conn               Opens the connection with the database
    @param cur                Initialise the cursor which accesses the databse
    @param query              Initialises the SQL qeury
    @param cur.execute(query) Executes an sql query with the data stored in the query parameter
    @param data               Stores the data from the query
    @param cur.close()        Closes the access to the database
    @param conn.close()       Closes the connection to the database
    @return                   Returns the data that is fetched
'''
def fetchChart1y():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT distance_travelled FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
'''
fetchChart1x() function is to fetch the data from the dashboard table in the coolmotor database
to be used in the x axis of the 1st chart
    @param conn               Opens the connection with the database
    @param cur                Initialise the cursor which accesses the databse
    @param query              Initialises the SQL qeury
    @param cur.execute(query) Executes an sql query with the data stored in the query parameter
    @param data               Stores the data from the query
    @param cur.close()        Closes the access to the database
    @param conn.close()       Closes the connection to the database
    @return                   Returns the data that is fetched
'''
def fetchChart1x():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT entry_id FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

'''
fetchChart2y() function is to fetch the data from the dashboard table in the coolmotor database
to be used in the y axis of the 2nd chart
    @param conn               Opens the connection with the database
    @param cur                Initialise the cursor which accesses the databse
    @param query              Initialises the SQL qeury
    @param cur.execute(query) Executes an sql query with the data stored in the query parameter
    @param data               Stores the data from the query
    @param cur.close()        Closes the access to the database
    @param conn.close()       Closes the connection to the database
    @return                   Returns the data that is fetched
'''
def fetchChart2y():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT game_duration FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

'''
fetchChart2x() function is to fetch the data from the dashboard table in the coolmotor database
to be used in the x axis of the 2nd chart
    @param conn               Opens the connection with the database
    @param cur                Initialise the cursor which accesses the databse
    @param query              Initialises the SQL qeury
    @param cur.execute(query) Executes an sql query with the data stored in the query parameter
    @param data               Stores the data from the query
    @param cur.close()        Closes the access to the database
    @param conn.close()       Closes the connection to the database
    @return                   Returns the data that is fetched
'''
def fetchChart2x():
    conn = mysql.connector.connect(host=constants.HOST,
                                   database=constants.DATABASE,
                                   user=constants.USER,
                                   password=constants.PASSWORD)
    cur = conn.cursor()
    query = ("SELECT date FROM dashboard;")
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data