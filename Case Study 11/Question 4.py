# Insert values into the customer table and display the contents.
# (1001, 34, 'Austin', 'male'),(1002, 37, 'Houston', 'male'),(1003, 25, 'Austin', 'female'),(1004, 28, 'Houston', 'female'),(1005, 22, 'Dallas', 'male')

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()

insert_query = "INSERT INTO customer(Id,Age,Country,Gender) values(%s,%s,%s,%s)"
values = [(1001, 34, 'Austin', 'male'),(1002, 37, 'Houston', 'male'),(1003, 25, 'Austin', 'female'),(1004, 28, 'Houston', 'female'),(1005, 22, 'Dallas', 'male')]
cursor.executemany(insert_query, values)
print(cursor.rowcount,"record inserted.")

select_query = "SELECT * FROM customer;"
cursor.execute(select_query)
for record in cursor.fetchall():
    print("*"*20)
    print("Id :",record[0])
    print("Country :",record[1])
    print("Age :",record[2])
    print("Gender :",record[3])
    print("*"*20)

connection.commit()
connection.close()