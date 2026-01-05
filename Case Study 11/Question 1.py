# Create a database called retails.

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE RETAILS")
connection.close()