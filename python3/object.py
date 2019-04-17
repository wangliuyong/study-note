'''
对象的特征
0.类
1.多态
2.继承
'''

# 1.类 class通常大写开头

##定义一个类
class People:
    #属性
    name="wang"
    age=18
    #方法
    def run(self,name): #self指的是生成的对像实列，就是this
        self.name=name
        print('run')

print(People)



class Ball:
    name="wang"
    def __init__(self,name):  #类似于构造函数constructor()
        self.name=name
    def print_name(self):
        print('我的名字是：%s' % self.name)

me=Ball('wangliuyong')
me.print_name()

## __name形式的都是对象私有的方法或者属性，外部无法访问，只能通过内部惊醒访问，例如  通过self去访问。私有的不会被后代所继承
class People2:
    #属性
    _name="wang"
    _age=18
    #方法
    def run(self,name): #self指的是生成的对像实列，就是this
        self.name=name
        print('run')

print(People)

# 继承一个类
class Man(People):
    pass

print(Man)


