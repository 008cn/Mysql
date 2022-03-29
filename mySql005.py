import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)  # 执行SQL语句
    db.commit()  # 提交到数据库执行
except:
    db.rollback()  # 发生错误时回滚

# 关闭数据库连接
db.close()
