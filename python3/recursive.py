# 递归

#迭代函数
def getProduct(n):
    product = 1
    for i in range(1,n+1):
        product *= i 
    
    print("%d的阶乘是%d:" % (n,product))
    return product

getProduct(10)

# 递归函数
def getProduct1(n):
    if n == 1:
        return 1
    else:
        return getProduct1(n-1) *n

getProduct1(3)

#斐波那契数列

n = int(input('输入数列的项数：'))

a, b, count= 0, 1, 0
while True:
    if count < n:
        print(b)
        a, b = b, a+b
        count += 1
    else:
        break