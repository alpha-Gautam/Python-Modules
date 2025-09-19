# sqlite3 - Built-in Library for SQLite
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
