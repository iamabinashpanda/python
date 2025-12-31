import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="PythonTraining"
)
cursor = connection.cursor()
query = "CREATE TABLE student (personID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),age INT);"
cursor.execute(query)
cursor.execute("SHOW TABLES")
result = cursor.fetchall()
print(result)