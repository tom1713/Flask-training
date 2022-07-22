import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://root:root123@cluster0.hpcbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mywebsite
collection = db.users

cur = collection.find({
     "$or" : [
          {"email" : "peng@peng.com"},
          {"level" : 4}
     ]
}, sort = [
     ("level", pymongo.ASCENDING)
])
for doc in cur:
     print(doc)
# doc = collection.find_one({
#      "$and" : [
#           {"email" : "john@john.com"},
#           {"password" : "john"}
#           ]
# })
# print("取得的資料", doc)

# result = collection.delete_many({
#      "level" : 5
# })
# print("實際上刪除的資料有幾筆",result.deleted_count)
# result = collection.delete_one({
#      "email" : "test3@test3.com"
# })
# print("實際上刪除的資料有幾筆",result.deleted_count)

# result = collection.update_many({
#      "level" : 1,
# }, {"$set" : {
#      "level" : 4
# }})
# print("符合條件的文件數量:", result.matched_count)
# print("實際更新的文件數量:", result.modified_count)

# result = collection.update_one({
#      "email" : "peng@peng.com"
# }, {"$mul":{
#      "level" : 0.5
# }})
# print("符合條件的文件數量:", result.matched_count)
# print("實際更新的文件數量:", result.modified_count)

# cursor = collection.find()
# print(cursor)
# for doc in cursor:
#      print(doc["name"])
# data = collection.find_one(ObjectId("627b3b662fc9722e16de0aef"))
# print(data)
# data = collection.find_one()
# print(data["_id"])
# print(data["name"])
# data = collection.find_one()
# print(data)

# result = collection.insert_many([{
#      "name" : "測試資料1",
#      "email" : "test1@test1.com",
#      "password" : "test1",
#      "level" : 5    
# }, {
#      "name" : "測試資料2",
#      "email" : "test2@test2.com",
#      "password" : "test2",
#      "level" : 5   
# },{
#      "name" : "測試資料3",
#      "email" : "test3@test3.com",
#      "password" : "test3",
#      "level" : 5 

# }])
# # result = collection.insert_one({
# #     "name" : "丁滿",
# #     "email" : "ding@ding.com",
# #     "password" : "ding",
# #     "level" : 1
# # })
# print("資料新增成功")
# print(result.inserted_ids)