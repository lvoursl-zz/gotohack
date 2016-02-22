import pymongo

client = pymongo.MongoClient('goto.reproducible.work')
db = client['vk_bukin']
users = db['users']

print(users.find({'_id' : '1'}))
