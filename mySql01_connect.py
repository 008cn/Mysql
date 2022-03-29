from pymysql import connect

db = connect(host='localhost',
             port=3307,
             user='root',
             passwd='123456',
             db='guest_test',
             charset='utf8')  # 打开数据库连接
try:
    with db.cursor() as cursors:
        sql = 'SELECT * FROM students;'
        cursors.execute(sql)
        db.commit()  # 提交事务到数据库
        result = cursors.fetchmany(3)  # 接收前3行数据
        print(result)
finally:
    db.close()
