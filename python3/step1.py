#模块循环输入

import random
script = random.randint(1,10)

print("王刘永是个大帅哥")
temp=input("猜猜看我在想什么数字呢\n")  #获取一个输入
guess=int(temp) #将变量转换成整型

while guess != script:
    
    if guess > script :
        print("big")
    else:
        print("small")
    temp=input("继续输入:\n")
    guess=int(temp)
#断言
assert( False if guess == script else True)
print("猜到了,正确答案是："+ str(script))
print("game over" )