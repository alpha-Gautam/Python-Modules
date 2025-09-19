# mysql-connector-python - Official MySQL Driver
#
# This library is the official, pure Python driver for connecting to MySQL databases.
# It is developed and supported by Oracle.
# You need to install it with `pip install mysql-connector-python` and have a MySQL server running.

import mysql.connector

# You must replace these with your MySQL credentials and database name
CONFIG = {
    'host': '127.0.0.1',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'test_db'
}

try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(**CONFIG)
    cursor = conn.cursor()

    # Drop and create a new table
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50));")

    # Insert a record
    cursor.execute("INSERT INTO employees (id, name) VALUES (%s, %s)", (1, 'Alice'))
    conn.commit()

    # Query the table
    cursor.execute("SELECT * FROM employees;")
    print("Fetched from mysql-connector-python:")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print(f"MySQL error: {err}")
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
