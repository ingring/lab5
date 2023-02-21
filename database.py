from pymongo import MongoClient
import os

# MONGOUSER = 'mongo'
# MONGOPASSWORD = 'Oqzfv0GRj9ha34InGfXP'
# MONGOHOST = 'containers-us-west-152.railway.app'
# MONGOPORT = 5676


client = MongoClient('mongodb://mongo:Oqzfv0GRj9ha34InGfXP@containers-us-west-152.railway.app:5676')
db = client.get_default_database()

