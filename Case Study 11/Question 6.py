# Group customers based on location and display the information.

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
cursor.execute("SELECT country,count(id) FROM customer group by country")
for city,id in cursor.fetchall():
    print(f"City : {city}, # of people : {id}")

connection.close()
