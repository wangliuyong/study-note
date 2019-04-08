#字典类似于对象

dic={"name":"wang","age":18}
dic['namedic']
#add
dic['xingbie'] = 'man'

del dic['Name'] # 删除键 'Name'
dic.clear()     # 清空字典
del dic         # 删除字典

dic.keys()
dic.items()
dic.values
dic.get()
b=dic.copy() #浅拷贝,另存了一份，不是直接复制地址
c=b.update(b)

#  set集合
