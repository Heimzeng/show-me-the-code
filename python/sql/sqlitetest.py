import sqlite3
import os
import random

def createTableIfNotExists(conn, tablename, paras):
    try:
        sql = "create table if not exists " + tablename + " ("
        for para in paras:
            sql = sql + para + ", "
        sql = sql[:-2]
        sql = sql + ")"
        conn.execute(sql)
    except Exception as e:
        raise e

def insert(conn, tablename, paras):
    try:
        sql = "insert into " + tablename + " values ("
        for para in paras:
            sql = sql + "'" + str(para) + "', "
        # 多了个逗号会报错，so do this
        sql = sql[:-2]
        sql = sql + ")"
        conn.execute(sql)
        conn.commit()
    except Exception as e:
        raise e

def checkFileExist(file_path):
    return os.path.isfile(file_path)

if __name__ == '__main__':
    dbname = './user.db'
    tablename = 'user'
    connection = sqlite3.connect(dbname)
    createTableIfNotExists(connection, tablename, ['PID INT NOT NULL', 'USERNAME VARCHAR(32)', 'SCORE INT'])
    '''
    for i in range(1000):
        insert(connection, tablename, [0, 'heim', random.randint(0, 1000)])
    '''
    sql = "select * from user"
    users = connection.execute(sql)
    print(users)
    for user in users:
        print(user)
    sql = 'select * from user order by score desc limit 10 offset 0'
    users = connection.execute(sql)
    print(users)
    for user in users:
        print(user)
    connection.close()