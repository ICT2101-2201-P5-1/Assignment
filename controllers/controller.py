import mysql.connector
from mysql.connector import errorcode
import models.model

def controller():
    models.model.test()