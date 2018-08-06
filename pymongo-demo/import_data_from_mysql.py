import pymysql
import pymongo

# 从mysql中把数据取出来，存入mongodb中

# 1. 从mysql中取数据
# a. 连接mysql
con = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='liuhe')
# b. 获取游标(指定数据结果是字典格式)
cur = con.cursor(cursor=pymysql.cursors.DictCursor)
# c. 定义SQL语句
sql = 'select * from class'
# d. 执行SQL语句
try:
    cur.execute(sql)
    # e. 获取结果集合
    results = cur.fetchall()
    # 2. 把数据存入mongodb
    print(results)
    # a. 连接mongodb
    client = pymongo.MongoClient(host='localhost', port=27017)
    # b. 获取数据库
    db = client.ai11
    # c. 获取集合
    collection = db.classes
    # d. 执行数据添加
    res = collection.insert_many(results)
    # f. 关闭数据库连接
    client.close()
except Exception as e:
    raise e
finally:
    con.close()

