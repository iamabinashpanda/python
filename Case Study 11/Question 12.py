# Count the number of distinct days in the data

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
cursor.execute("SELECT COUNT(DISTINCT OrderDate) FROM `orders`")
print(cursor.fetchall()[0][0])

connection.close()