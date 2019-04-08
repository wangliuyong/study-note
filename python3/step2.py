#判断语句

k=dir(__builtins__)    #输出所有的内建函数
print(k)
name=input("请输入您的名字：\n")
print("您的名字是："+name)
print('"c:\n 6666"')
print(r'"c:\n 6666"')  #r后面代表跟的是原始字符串
##三重引号字符串
print("""
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
# """)
# 判断数据的类型
# 1.type()2.isinatance("name",str)=>true
#三元操作符
y = 4
x = 4
if x < y:
    small=x
else:
    small = y
#三元操作符
small = x if x < y else y