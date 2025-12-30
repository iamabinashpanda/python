import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
result = cursor.fetchall()
print(result)
