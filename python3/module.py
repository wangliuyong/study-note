# 模块
import sys
sys.path.append('.\\module')
# import function

from function import myClass

print('myClass:', myClass(1,5))

# print('参数是：')
# for i in sys.argv:
#     print(i)

# print('该模块的路径是：',sys.path)

# # __name__属性
# # 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

# #!/usr/bin/python3
# # Filename: using_name.py

# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
# # 运行输出如下：

# # $ python using_name.py
# # 程序自身在运行
# # $ python
# # >>> import using_name
# # 我来自另一模块
# # >>>

# #  1.import sys
# #  2.sys.path.append("D:\\test")