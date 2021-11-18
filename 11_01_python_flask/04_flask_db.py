import pymongo
from pymongo import collection

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test2
collection = db.orders

# collection.insert_many([
#    { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
#    { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "A" },
#    { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
#    { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
#    { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" }
# ])

# id를 원하는 대로 추가하기
collection.insert_many([
    { "_id": 1, "item": { "category": "cake", "type": "chiffon" }, "amount": 10 },
    { "_id": 2, "item": { "category": "cookies", "type": "chocolate chip" }, "amount": 50 },
    { "_id": 3, "item": { "category": "cookies", "type": "chocolate chip" }, "amount": 15 },
    { "_id": 4, "item": { "category": "cake", "type": "lemon" }, "amount": 30 },
    { "_id": 5, "item": { "category": "cake", "type": "carrot" }, "amount": 20 },
    { "_id": 6, "item": { "category": "brownies", "type": "blondie" }, "amount": 10 }
])


results = collection.find().sort('_id', 1)

for r in results:
    print(r)