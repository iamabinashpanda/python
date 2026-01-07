# Add a new ‘is_sale’ column in ‘orders’ table.

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="retails"
)
cursor = connection.cursor()
cursor.execute("ALTER TABLE orders ADD COLUMN is_sale BOOLEAN DEFAULT FALSE;")
connection.commit()
connection.close()