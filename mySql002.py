import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3307,
                     user='root',
                     passwd='123456',
                     db='guest_test',
                     charset='utf8')  # 打开数据库连接

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
db.commit()

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
db.commit()

# 关闭数据库连接
db.close()
