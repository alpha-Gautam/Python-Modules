# pymongo - Official MongoDB Driver
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

