import certifi as certifi
from pymongo import MongoClient


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://shrikesh:XtRWfLdLx7PGtHOi@cluster0.mvbesl9.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())

    # Return the Database of our interest
    return client['sample_mflix']


if __name__ == "__main__":
    dbname = get_database()

