from pymongo import MongoClient
import os

client = MongoClient(os.getenv('mongodb://mongo:Oqzfv0GRj9ha34InGfXP@containers-us-west-152.railway.app:5676'))
db = client.get_default_database()

