from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://hailieformosae22027_db_user:eZDyarcysXaHQI3y@databasedeployments.glu6ktw.mongodb.net/?appName=DatabaseDeployments"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
