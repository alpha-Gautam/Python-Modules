# sqlalchemy - Python SQL Toolkit and ORM
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
