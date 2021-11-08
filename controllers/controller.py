import mysql.connector
from mysql.connector import errorcode
import models.model

query = ("SELECT pw FROM accounts")

def controller():
    models.model.test(query)