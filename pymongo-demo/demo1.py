# 导入包
import pymongo
# 连接mongodb
client = pymongo.MongoClient(host='localhost', port=27017)
# 获取数据库：client.数据库名，如果数据库名是非法标识符名称，则需要
# 以client['数据库名']的方式访问
db = client.ai11
# 获取集合：db.集合名
collection = db.student
# 执行数据CRDU操作（操作方法与命令行里的方法一致）
res = collection.find({'name':'张三'})
# 遍历查询结果集
for row in res:
    print(row)
# 关闭连接
client.close()
