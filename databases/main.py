import os

# Define the folder name and file contents
folder_name = 'database_python_library'
files_to_create = {
    'sqlite3.py': """# sqlite3 - Built-in Library for SQLite
#
# This module is part of Python's standard library and provides a DB-API 2.0 compliant
# interface for working with SQLite databases. It is useful for small-scale applications
# and testing because it requires no separate database server and stores data in a single file.

import sqlite3

try:
    # Connect to the database (creates a new file if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute("CREATE TABLE IF NOT EXISTS stocks (date TEXT, symbol TEXT, price REAL)")

    # Insert some data
    cursor.execute("INSERT INTO stocks VALUES ('2025-09-20', 'GOOG', 150.00)")
    conn.commit()

    # Query the data
    cursor.execute("SELECT * FROM stocks")
    print("Fetched from sqlite3:")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
finally:
    # Always close the connection
    if conn:
        conn.close()
""",
    'psycopg.py': """# psycopg - PostgreSQL Adapter for Python
#
# Psycopg is the most popular PostgreSQL database adapter for the Python language.
# Psycopg 3 is the modern, new generation version with full asynchronous support.
# You need to install it with `pip install psycopg` and have a PostgreSQL server running.

import psycopg

# You must replace these with your PostgreSQL credentials and database name
# Ensure a PostgreSQL database named 'test_db' and a table exist, or adjust the code.
DB_NAME = "test_db"
DB_USER = "postgres"
CONN_STRING = f"dbname={DB_NAME} user={DB_USER}"

try:
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            # Drop and create a new table for a clean example
            cur.execute("DROP TABLE IF EXISTS sales;")
            cur.execute("CREATE TABLE sales (id SERIAL PRIMARY KEY, item VARCHAR(50), quantity INT);")

            # Insert a record
            cur.execute("INSERT INTO sales (item, quantity) VALUES (%s, %s)", ('book', 5))

            # Query the table
            cur.execute("SELECT * FROM sales;")
            print("Fetched from psycopg:")
            for record in cur.fetchall():
                print(record)
except psycopg.OperationalError as e:
    print(f"Operational error connecting to PostgreSQL: {e}")
    print("Please ensure PostgreSQL is running and your connection details are correct.")

""",
    'mysql_connector_python.py': """# mysql-connector-python - Official MySQL Driver
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
""",
    'pymongo.py': """# pymongo - Official MongoDB Driver
#
# PyMongo is the official driver for MongoDB, a popular NoSQL document database.
# It provides an idiomatic, Pythonic way to work with MongoDB and its BSON format.
# You need to install it with `pip install pymongo` and have a MongoDB server running.

import pymongo

# You must ensure a MongoDB server is running at this address
client = pymongo.MongoClient("mongodb://localhost:27017/")

try:
    # Access a database and a collection
    db = client["mydatabase"]
    collection = db["mycollection"]

    # Insert a document
    document = {"name": "Bob", "age": 35, "city": "New York"}
    insert_result = collection.insert_one(document)
    print(f"Inserted document ID: {insert_result.inserted_id}")

    # Find the document
    found_document = collection.find_one({"name": "Bob"})
    print("Found document with pymongo:")
    print(found_document)

except pymongo.errors.ConnectionFailure as e:
    print(f"MongoDB connection failed: {e}")
    print("Please ensure your MongoDB server is running.")

""",
    'sqlalchemy.py': """# sqlalchemy - Python SQL Toolkit and ORM
#
# SQLAlchemy is a powerful and flexible library that provides a high-level,
# object-oriented approach (ORM) and a lower-level SQL expression language
# for interacting with many different types of databases. It requires a specific
# DB-API driver (like `sqlite3`, `psycopg`, or `mysql-connector-python`) to connect.
# You need to install it with `pip install sqlalchemy`.

from sqlalchemy import create_engine, text, Table, MetaData, Column, Integer, String

# --- Core Usage Example ---

# In this example, we use a SQLite database
engine = create_engine('sqlite:///sqlalchemy_example.db')

try:
    with engine.connect() as conn:
        # Define and create a table using Core
        meta = MetaData()
        users_table = Table(
            'users', meta,
            Column('id', Integer, primary_key=True),
            Column('name', String)
        )
        meta.create_all(engine)

        # Insert data using Core's expression language
        conn.execute(users_table.insert(), {'id': 1, 'name': 'Charlie'})
        conn.commit()

        # Query data with text-based SQL
        result = conn.execute(text("SELECT * FROM users"))
        print("Fetched from SQLAlchemy (Core):")
        for row in result:
            print(row)

except Exception as e:
    print(f"SQLAlchemy error: {e}")

# Note: The ORM usage is more complex and not included in this simple example.
# It involves declarative base classes and session management.
"""
}

# Create the main directory if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Created directory: {folder_name}")
else:
    print(f"Directory '{folder_name}' already exists.")

# Create and populate the files
for file_name, content in files_to_create.items():
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Created file: {file_path}")

print("\nTask complete. The directory and files have been generated.")
