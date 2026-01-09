# Show the details of customers who are located in Austin City.
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
city = "Austin"
select_query = f"select * from customer where country = '{city}'"
cursor.execute(select_query)
for record in cursor.fetchall():
    print(record)
    print("*"*20)