k = {'username': 'xiao', 'password': '123'}
ks = [{'username': 'xiao', 'password': '123'}, {'username': 'xiao', 'password': '123'}]

import pymongo

client = pymongo.MongoClient()  # 连接
db = client.get_database("2020-08-26")  # 有就使用 没有就创建
c = db.get_collection('c1')
c.insert_one(k)
c.insert_many(ks)

gen = c.find()  # 数据生成器
for data in gen:
    print(data)
