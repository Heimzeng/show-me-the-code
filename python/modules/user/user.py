import sqlite3
import bcrypt
class UserManager:
    def __init__(self):
        self.dbname = './user.db'
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
            ID INT PRIMARY KEY NOT NULL,
            NAME CHAR(12)  NOT NULL,
            PASSWORD CHAR(60) NOT NULL
            );''')
        self.conn.commit()
        # self.conn.close()
    def addUser(self,user):
        res = self.cursor.execute('SELECT * FROM USER WHERE NAME=?', (user['name'], ))        
        if len(list(res)) != 0:
            return 2 # user exists
        res = self.cursor.execute('SELECT ID FROM USER ORDER BY ID DESC LIMIT 1') 
        id = 0
        res = list(res)

        if len(res) > 0:
            id = res[0][0]+1  
        try:
            self.cursor.execute('INSERT INTO USER (ID,NAME,PASSWORD) \
            VALUES (?, ?, ?)', (id, user['name'], bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt())))
            self.conn.commit()
            return 0 # succ
        except:
            return 1 # unknow error
    def checkUser(self,user):
        res = self.cursor.execute('SELECT * FROM USER WHERE NAME=?', (user['name'], ))
        res = list(res)
        if len(res) > 0:
            hashedPassword = res[0][2]
            if bcrypt.checkpw(user['password'].encode('utf-8'), hashedPassword):
                return 0
            else:
                return 1
        else:
            return 404
    def getAllUsers(self):
        return list(self.cursor.execute('SELECT * FROM USER'))
    def updatePassword(self,user):
        try:
            self.cursor.execute('UPDATE USER SET PASSWORD = ? WHERE NAME = ?', (user['password'], user['name']))
            self.conn.commit()
            return 0
        except:
            return 1
if __name__ == '__main__':
    userMng = UserManager()
    res = userMng.addUser({'name':'heim3', 'password':'zeng'})
    print(res)
    userMng.checkUser({'name':'heim'})
    users = userMng.getAllUsers()
    print(users)
    userMng.updatePassword({'name':'heim3', 'password':'zeng3'})
    users = userMng.getAllUsers()
    print(users)