# QQ群发消息

import win32api,win32con,win32gui
import os
import time
import random
import win32clipboard

import public.keybordAndMouse as keybordAndMouse
import public.qqPublic as qqPublic
import public.allPublic as allPublic
import public.qqJoinGroup as qqJoinGroup
import public.qqGroupMsg as qqGroupMsg

# python D:\winAutoPython\myprogect\sendQQGroupMsgTask.py

# 消息
groupMsgs = ('晚餐吃太饱了总么办','555...', '嘻','玩全民K歌')

qqIds = {'486548267':'mystery3002'}

# 把所有的消息都发送到所有的QQ号码后，就自动终止，而且每给一个QQ轮发一个消息后，就休眠一段时间
for msg in groupMsgs:

	for qq in qqIds:

		# 登录
		password = qqIds[qq]
		qqPublic.login(qq,password) 
		# 写日志
		log = '成功登录QQ:'+str(qq)
		allPublic.writeLog(log)

		# 登录QQ后 休眠1-5分钟
		#randMin = random.randint(1,5)
		#time.sleep(randMin*60)

		# 发群消息		
		qqGroupMsg.send(msg); 

		# 一条群消息发送给一个QQ的所有群之后 休眠1-5分钟
		randMin = random.randint(1,2)
		time.sleep(randMin*3)
		
		#退出本QQ--准备切换QQ号码，再发送本条消息，并且休眠30-60分钟
		qqPublic.logExit();
		allPublic.writeLog('本轮任务执行完成，QQ已成功关闭，下一个任务稍后执行，请勿关闭窗口')
		randMin = random.randint(30,60)
		time.sleep(randMin*60)

allPublic.writeLog('本此任务全部执行完毕，可以关闭窗口进行其他操作了')