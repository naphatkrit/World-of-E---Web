import json
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('107.170.47.250');
db = client.world_of_e_data;
collection_learn = db.world_of_e_learn
collection_do = db.world_of_e_do
collection_connect = db.world_of_e_connect
collection_all_data = db.world_of_e_all_data