# CRUD Python Module for the Grazioso Salvare Animal Shelter Database

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is hard-wired to use the aac
        # database, the animals collection, and the aac user.
        #
        # You must edit the password below for your environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        """Insert a document into the MongoDB collection"""

        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create Error:", e)
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, query):
        """Query documents from the MongoDB collection"""

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print("Read Error:", e)
            return []
        
            # Update method to implement the U in CRUD
    def update(self, query, new_values):
        """Update document(s) in the MongoDB collection"""

        try:
            result = self.collection.update_many(query, new_values)
            return result.modified_count

        except Exception as e:
            print("Update Error:", e)
            return 0

    # Delete method to implement the D in CRUD
    def delete(self, query):
        """Delete document(s) from the MongoDB collection"""

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except Exception as e:
            print("Delete Error:", e)
            return 0