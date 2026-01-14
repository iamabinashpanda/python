# Insert values into the orders table and display the contents
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
query = "INSERT INTO orders (OrderDate,Price,ID) VALUES (%s,%s,%s)"
values = [('2022-10-1', 100.25, 1),('2022-10-2',200.75, 2),('2022-10-3',500.00,3),('2022-10-3', 600.00,4),('2022-10-4', 600.00,5)]
cursor.executemany(query, values)
connection.commit()

cursor.execute("SELECT * FROM orders")
for records in cursor.fetchall():
    print("Id :",records[0])
    print("Order Date :",records[1])
    print("Price :",records[2])

connection.close()