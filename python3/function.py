#定义
def myClass(a,b):
    '这里是文档'
    print('first function')
    return a + b

#调用
myClass(1,2)
#查看函数定义的文档
myClass.__doc__

#关键字参数
myClass(a = 1, b = 2)
#默认参数
def myClass2(a=0,b=0):
    '这里是文档'
    print('first function')
    return a + b

#收集参数
def test(*params):
    return 0

# 在函数内部不要随便修改全局变量
name = "wang"
def test1():
    name = "liu" #此时会创建一个name局部变量，全局的name并不会改变
# 如果需要修改全局变量请使用globl关键字
name = "wang"
def test2():
    global name
    name = "liu" 

# 闭包的应用 使用nolocal 关键字
def fun1():
    name = "liu"
    def fun2():
        nonlocal name
        name = "wang"
        return 0
    fun2()
    print(name)
    return 0
fun1()