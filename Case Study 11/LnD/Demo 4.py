import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="PythonTraining"
)

cursor = connection.cursor()
query = "INSERT INTO Student (name,age) VALUES (%s, %s)"
values = [("Malay",30),("Sachin",29),("Aswini",28),("Heetashree",31)]
cursor.executemany(query,values)
connection.commit()
print(cursor.rowcount,"record inserted.")