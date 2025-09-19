# psycopg - PostgreSQL Adapter for Python
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

