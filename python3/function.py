#函数

if __name__ == "__main__":
    def myClass2(a=0,b=0):
        '这里是文档'
        print('first function')
        return a + b

    print(myClass2.__doc__)
    #收集参数
    def test(*params):
        print('*params:', *params)
        return 0
    test(1,2,3)
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
            return name
        print(name)
        return fun2()
    fun1()
    # lambda表达式，其实就是匿名函数
    d = lambda x, y : x+y
    d(2,3)

    # filter 过滤器
    temp = range(10)
    list(filter(lambda x : x % 2,temp))

    # map 迭代器
    temp = range(10)
    list(map(lambda x : x ** 2,temp))

    # 迭代器对象

    i = iter([1,2,3,4])
    next(i)

    for item in i:
        print(item)
else:
    print('另一个模块')
    #定义
    def myClass(a,b):
        '这里是文档'
        print('first function')
        return a + b

    #调用
    # myClass(1,2)
    #查看函数定义的文档
    myClass.__doc__

    #关键字参数
    # myClass(a = 1, b = 2)
    #默认参数


