# Group customers based on their gender and display the information.

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
cursor.execute("SELECT gender,count(id) FROM customer group by gender")

print(cursor.fetchall())