import hashlib
import web
import receive
import reply
import requests
import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute('create table if not exists user (openid varchar(28) primary key, coins int, inveteropenid varchar(28))')
cursor.close()
conn.commit()
conn.close()

appid = "wxbbac27a3d70fff1c"
appsecret = "f6db897c66deaafb59e5e829aae5e509"
state = {}
class Handle(object):
	access_token = None
	def getStarNickName(self, name):
		name = name.decode(encoding='utf-8')
		if len(name) >= 6:
			return None
		else:
			return '\u2061' + name
	def getReplyContent(self, fromUser, userInput):
		if self.access_token == None:
			r = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxbbac27a3d70fff1c&secret=f6db897c66deaafb59e5e829aae5e509")
			self.access_token = r.json()['access_token']
		if state.get(fromUser) == None or state[fromUser] == -1:
			state[fromUser] = 0
			return "欢迎使用本公众号，请选择功能：\n1、王者荣耀明星昵称\n2、长截>图小程序\n3、Ins图片下载\n4、我的推广码"
		elif state[fromUser] == 0:
			if userInput in [b"2", b"3", b"4"]:
				return "此功能尚未推出，敬请期待"
			elif userInput == b"1":
				state[fromUser] = 1
				return "请输入您要仿造的名字"
			else:
				print("userInput error, userInput is:")
				print(userInput)
				return "userInput error"
		elif state[fromUser] == 1:
			conn = sqlite3.connect("app.db")
			cursor = conn.cursor()
			cursor.execute('select coins from user where openid = ?', (fromUser,))
			values = cursor.fetchall()
			coins = values[0][0]
			if coins <= 0:
				cursor.close()
				conn.close()
				return "积分不足"
			print("get values: ", values)
			nickName = self.getStarNickName(userInput)
			if nickName == None:
				return "名字过长，请重试"
			else:
				cursor.execute('update user set coins = ? where openid = ?', (coins - 1, fromUser,))
				cursor.close()
				conn.commit()
				conn.close()
				state[fromUser] = -1
				return nickName
	def GET(self):
		try :
			data = web.input()
			if len(data) == 0:
				return "data empty"
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "hello2019"
			list = [token, timestamp, nonce, ""]
			list.sort()
			sha1 = hashlib.sha1()
			sha1.update(''.join(list).encode())
			hashcode = sha1.hexdigest()
			if hashcode == signature:
				return echostr
			else:
				return ""
		except Exception:
			return ""
	def POST(self):
		try:
			webData = web.data()
			print("Handle Post webdata is ", webData)
			recMsg = receive.parse_xml(webData)
			fromUser = recMsg.FromUserName
			toUser = recMsg.ToUserName
			userInput = recMsg.Content
			conn = sqlite3.connect("app.db")
			cursor = conn.cursor()
			cursor.execute('select * from user where openid = ?', (fromUser,))
			if len(cursor.fetchall()) == 0:
				cursor.execute('insert into user values (?, ?, "")', (fromUser, 1, ))
			cursor.close()
			conn.commit()
			conn.close()
			print("recv msg:", userInput)
			if recMsg.MsgType == 'text':
				content = self.getReplyContent(fromUser, userInput)
				print("reply: ", content)
				replyMsg = reply.TextMsg(fromUser, toUser, content)
				return replyMsg.send()
			else:
				print("reply nothing")
				return ""
		except Exception:
			print("something went wrong.")
			return ""