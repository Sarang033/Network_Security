
from pymongo import MongoClient
from pymongo.server_api import ServerApi   # if you’re using Stable API with MongoDB Atlas

uri = "mongodb+srv://sarangchamp2004:<password>@cluster0.lxroneg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)