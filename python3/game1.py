import easygui as g
import random

g.msgbox('嗨，欢迎进入第一个界面小游戏！')
secret = random.randint(1,10)

msg = "猜猜我心中的数字是什么(0~10)："
title = "数字小游戏"
guess = g.integerbox(msg, title, lowerbound = 0, upperbound = 10)

while True:
    if guess == secret:
	    g.msgbox('你是我肚里的蛔虫吗！')
	    break
    else:
	    if guess > secret:
	    	g.msgbox('猜大了呀，再试试')
	    else:
	    	g.msgbox('猜小了呀，再试试')
	    guess = g.integerbox(msg, title, lowerbound = 0, upperbound = 10)

g.msgbox('游戏结束，不玩啦！')