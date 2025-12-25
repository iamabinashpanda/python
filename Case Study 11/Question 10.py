# Show orders that have an order amount of more than 300


import datetime as dt
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)

cursor = connection.cursor()
price = 300
cursor.execute(f"SELECT * FROM orders WHERE Price > {price}")
for id,date,price in cursor.fetchall():
    print(id,' - ',date,' - $',price)
connection.close()