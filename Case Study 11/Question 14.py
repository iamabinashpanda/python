# Calculate the average order amount for all days

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)

cursor = connection.cursor()
cursor.execute("SELECT AVG(Price) FROM orders")
print("$",cursor.fetchall()[0][0])
connection.close()