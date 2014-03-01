import json
import re
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('107.170.47.250')
db = client.world_of_e_data
collection_learn = db.world_of_e_learn
collection_do = db.world_of_e_do
collection_connect = db.world_of_e_connect
collection_all_data = db.world_of_e_all_data


def store_data():
    cell_information = json.loads(open("All.json").read())
    print "hello world";
    # below arrays are for checking whether or not something already exists.
    # not required until adding functions are used.

    #stores information into database
    collection_learn.insert(cell_information[0]);
    collection_do.insert(cell_information[1]);
    collection_connect.insert(cell_information[2]);
    collection_all_data.insert(cell_information);


def exportData(): 
	data = [];
	for section in collection_all_data.find():
		for content in section.get('sections'):
	 		for stuff in content.get('content'):
 	 			if stuff.get('url') is not None:
	 				fixed_URL = stuff.get('url');
	 				stuff['url'] = fixed_URL;
	 			if stuff.get('details') is not None:
	 				fixed_details = stuff.get('details')
	 				stuff['details'] = fixed_details
	 			if stuff.get('date') is not None:
	 				fixed_date = stuff.get('date')
	 				stuff['date'] = fixed_date
	 	data.append(section)
	with open('all_data_test.json', 'w') as outfile:
	    outfile.write(dumps(data, indent=3))

def exportSectionData(s):
	data = [{}]
	if s is "Learn":
		for section in collection_learn.find():
			data = section.get('sections')
	if s is "Do":
		for section in collection_do.find():
			data = section.get('sections')
	if s is "Connect":
		for section in collection_connect.find():
			data = section.get('sections')
	with open(s + '_data' + '.json', 'w') as outfile:
		outfile.write(json.dumps(data, indent=3))

store_data()
exportData()
# exportSectionData('Connect')

