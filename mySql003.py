import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3307,
                     user='root',
                     passwd='123456',
                     db='guest_test',
                     charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)  # 执行sql语句
    db.commit()  # 提交到数据库执行
except:
    db.rollback()  # 如果发生错误则回滚

# 关闭数据库连接
db.close()
