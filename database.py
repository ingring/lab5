from pymongo import MongoClient
import os

MONGOUSER = 'mongo'
MONGOPASSWORD = 'Oqzfv0GRj9ha34InGfXP'
MONGOHOST = 'containers-us-west-152.railway.app'
MONGOPORT = 5676


client = MongoClient(os.getenv('mongodb://${{ MONGOUSER }}:${{ MONGOPASSWORD }}@${{ MONGOHOST }}:${{ MONGOPORT }}'))
db = client.get_default_database()

