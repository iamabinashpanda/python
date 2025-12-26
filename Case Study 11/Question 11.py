# Show all orders placed on 2022-10-03 and represent it in sorted form with respect to the amount spent

import datetime as dt
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)

cursor = connection.cursor()
cursor.execute(f"SELECT * FROM orders WHERE OrderDate = '{dt.datetime.strptime("2022-10-03", "%Y-%m-%d").date()}' ORDER BY Price DESC")
for id,date,price in cursor.fetchall():
    print(id,' - ',date,' - $',price)
connection.close()
