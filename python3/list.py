list1 = ["wang","liu","yong"]
list2 = ["chen", 5,[4,5,6]]

#对列表的操作
# append("wang") 从列表尾部插入一个值
# extend(["wang",liuyong]) 尾部
# insert(startIndex,value) 指定index处插入
# remove(value) 一处特定的值
# del list1[0] 删除某个元素
# pop(index) 默认从头部插入
# reverse() 反转
# sort() 默认升序  sort(reverse=True)

#列表切片
# 常用于得到一个list的拷贝
# list1[2:8]
# list1[:]

list1 *= 3
print(list1)

print("wang" in list1)
print("wang" not in list1)
print(list2[2][1])
print(dir(list))

list1.count("wang")


