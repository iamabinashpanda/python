# Count the orders grouped by date

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)

cursor = connection.cursor()

cursor.execute("SELECT OrderDate,Count(id) FROM orders GROUP BY OrderDate")
for date,items in cursor.fetchall():
    print(date,items,":","items")

connection.close()