# Connect to the newly created database and create tables called customer and orders
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
customer_table ="CREATE TABLE customer(Id INT PRIMARY KEY,Country VARCHAR(100) NOT NULL,Age INT,Gender VARCHAR(6) CHECK (Gender IN ('male', 'female')));"
order_table = "CREATE TABLE Orders(ID INT PRIMARY KEY,OrderDate DATE,Price DECIMAL(10, 2));"
cursor.execute(customer_table)
cursor.execute(order_table)
connection.commit()
connection.close()