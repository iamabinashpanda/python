import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="PythonTraining"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM STUDENT")
for record in cursor.fetchall():
    print(record)