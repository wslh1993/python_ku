# 导入包
import pymongo
# 连接mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
# 获取数据库：client.数据库名，如果数据库名是非法标识符名称，则需要
# 以client['数据库名']的方式访问
db = client.ai11
# 获取集合：db.集合名
collection = db.student
# 查询年龄大于18的学生信息
# res = collection.find({'age': {'$gt': 18}})
# 查询年龄大于18并且小于25的学生信息
res = collection.find({
    '$and': [
        {
            'age': {'$gt': 18}
        },
        {
            'age': {'$lt': 25}
        }
    ]
})
for row in res:
    print(row)

client.close()


