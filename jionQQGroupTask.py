# QQ群批量加群

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
import config

# python e:\winAutoPython\myprogect\jionQQGroupTask.py

# 关键词循环里面账号循环
# 关键词可以随意增加，一个QQ号码每次加一个地区，下次加其他地区，地区和其他的QQ不重复，和自己地区也不要重复，重复的话换验证消息
allList = {
			'qqGroupKeywords':['90后相亲','90后交友'], #搜群关键词
			'accounts':
			{
				'1':
				{
					'QQ':'2214385068',
					'password':'jiandan0321',
					'area':'深圳',
					'validaInfo':'找人聊天啊' # 加群验证信息
				}
			}		
}

# 关键词循环间隔秒数--关键词一天只执行一个，这样才可以保证下面的账号循环时，每个账号每天只会登录一次，并加10个以内的QQ
# 加多关键词，并长期执行才有意义
# QQ号多了才有意义
keywordTime = 60*60*24+60*60*1

# 账号循环间隔秒数
accountTime = 60*60*4

# 加群时换行总数量
rowsNum = 10

# 只加哪几行的QQ群不加，加群数量=元素个数*3，建议不要超过4个元素
jionRows = [2,3]

# 单个QQ加群间隔秒数
oneTime = 60*10

# 3个QQ加群时间间隔秒数
threeTime = 60*60*2


# 开始执行

qqGroupKeywords = allList.get('qqGroupKeywords')
accounts = allList.get('accounts')

# 循环群关键词
for qqGroupKeyword in qqGroupKeywords:
	# 循环账号
	for key in accounts:
		account = accounts.get(key)

		QQ = account.get('QQ')
		password = account.get('password')
		area = account.get('area')
		validaInfo = account.get('validaInfo')

		# 登录+休眠1-5分钟
		qqPublic.login(QQ,password) 
		log = '成功登录QQ:'+str(QQ)
		allPublic.writeLog(log)
		randSed = random.randint(1*60,5*60)
		time.sleep(randSed)

		# 加群 每次大概会加10个左右
		log = '预备加群信息：'+area+qqGroupKeyword+validaInfo
		allPublic.writeLog(log)
		qqJoinGroup.run(area,qqGroupKeyword,validaInfo,rowsNum,jionRows,oneTime,threeTime) 

		#退出+休眠1-5分钟
		qqPublic.logExit();
		allPublic.writeLog('本轮任务执行完成，QQ已成功关闭，下一个任务稍后执行，请勿关闭窗口')
		randSed = random.randint(1*60,5*60)
		time.sleep(randSed)

		#账号切换时休眠
		time.sleep(accountTime)

	#关键词切换时休眠
	time.sleep(keywordTime)

allPublic.writeLog('本此任务全部执行完毕，可以关闭窗口进行其他操作了')