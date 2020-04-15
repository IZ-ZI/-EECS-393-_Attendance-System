from pymongo import MongoClient
import pymongo

cluster = MongoClient(
    "mongodb+srv://wz:1999314Zwh%2F@attendancemanagementsystem-7immk.mongodb.net/test?retryWrites=true&w"
    "=majority")
db = cluster["AMS"]
collection = db["Administrator"]

post = {"_id": "123", "name": "sb", "email_address": "www.sb",
        "password": "wssb", "added_members": ["343", "435"], "pending_members": ["123"]}

post2 = {"_id": "456", "name": "sb", "email_address": "www.sb",
        "password": "wssb", "added_members": ["343", "435"], "pending_members": []}
#collection.insert_one(post)
#collection.insert_one(post2)



'''collection.update_one({"_id": "777"}, {'$set':
    {
        "name": "bb", "email_address": "www.bb",
        "password": "wsbb"
    }
})

collection.update_one(
            {"_id": "123"},
            {'$push': {"clubs": "456"}}
)'''

'''collection.update_one(
    {"_id": "123"},
    {'$pull': {"clubs": "123"}}
)'''
