#coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import requests, json
import os
import random

replyList = [u'你真棒', u'真的嘛？', u'然后呢', u'你是个傻逼', u'巧了你也是', u'儿子坐下']
peer_list = ['@@d7f9df73e0342d89774e08b3aca8e71182470b9d90a6f910710f3efba232a4b5']
# When recieve the following msg types, trigger the auto replying.
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True, isMpChat=True, isGroupChat=True)
def text_reply(msg):
    global auto_reply, robort_reply, peer_list
    print(msg['FromUserName'])
    print(msg['ToUserName'])
    # # The command signal of "[自动回复]"   
    # if msg['FromUserName'] == myUserName and msg['Content'] == u"开启自动回复":
    #     auto_reply = True
    #     itchat.send_msg(u"[自动回复]已经打开。\n", msg['FromUserName'])
    #     if msg['ToUserName'] not in peer_list:
    #         peer_list.append(msg['ToUserName'])
    # elif msg['FromUserName'] == myUserName and msg['Content'] == u"关闭自动回复":
    #     auto_reply = False
    #     itchat.send_msg(u"[自动回复]已经关闭。\n", msg['FromUserName'])
    # elif msg['FromUserName'] == myUserName and msg['Content'].find(u'add') != -1:
    #     replyList.append(msg['Content'][msg['Content'].find(u'add') + 3:])
    #     itchat.send_msg(u"已添加。\n", msg['FromUserName'])
    # else:    
    #     if auto_reply == True and msg['FromUserName'] in peer_list:
    #         r = int(random.randint(0, len(replyList)))
    #         itchat.send_msg(replyList[r], msg['FromUserName'])
    #     else:
    #         itchat.send_msg(msg['FromUserName'] + ':' + msg['Content'], myUserName)
    return


# Main
if __name__ == '__main__':
    # Set the hot login
    itchat.auto_login(enableCmdQR=True, hotReload=True)

    # Get your own UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print(myUserName)
    auto_reply = False
    robort_reply = False
    
    
    peers = itchat.get_friends(update=True)
    for peer in peers:
        print(peer['UserName'])
    print('peerssssssssssssss' + str(len(peers)))
    # itchat.send_msg(u'儿子们好', '@@d7f9df73e0342d89774e08b3aca8e71182470b9d90a6f910710f3efba232a4b5')
    
    rooms = itchat.get_chatrooms(update=True)
    for room in rooms:
        print(room['UserName'])
    print('roomsssssssssssssss' + str(len(rooms)))
    for room in rooms:
        if room['UserName'] == '@@0580b703a21e9805d28fc5d8d5daebdd7246dcc9613540105175cc0f9da0a6b5':
            print('get one')
            break
    itchat.run()