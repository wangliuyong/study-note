# pickle模块
# 将列表元组等序列格式转换成二进制格式
import pickle  

# 写入
my_list = [1,2,3,4]
pick_file = open('pickle_test.plk','wb')

pickle.dump(my_list,pick_file)
pick_file.close()

# 读取

pick_file = open('pickle_test.plk','rb')
my_list1 = pickle.load(pick_file)
pick_file.close()
print(my_list1)





