n=int(input('请输入层数：'))
def han(n,x='x',y='y',z='z'):
    if n == 1:
        print(x,'-->',y)
    else:
        han(n-1,x,z,y) #将前n-1个盘子移动到y上
        print(x,'-->',z) #将最后一个从X移动到z上
        han(n-1,y,z,x) # 将y上面的n-1个一定到z上


han(n)