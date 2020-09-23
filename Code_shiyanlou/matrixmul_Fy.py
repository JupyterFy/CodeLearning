'''
【题目】：
计算两个矩阵的 Hadamard 乘积。
要求输入矩阵的行/列数,在这里假设我们使用的是 n × n 的矩阵）
'''
############################################
'''
使用的语法糖：
列表推导式和input()和字符串的split()方法的结合

input()从键盘中读取输入，将其保存成一个字符串，紧接着使用split方法将其分割成字符型列表，
再通过int()强转成整型数组。
列表推导式的使用避免了定义空列表以及在for循环中使用append()组装整型数组的过程

split()方法语法
str.split(str="", num=string.count(str)).
该方法通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
'''
############################################
'''
【心得体会】：
一，熟练了使用列表推导式来组装列表（input()+int()强转+split()应该可以成为处理键盘输入的一大利器）；
二，通过使用enumerate函数，简化了获取相乘后的矩阵的计算过程；.

【不足之处】：
官方答案中使用了二维数组（列表），这种形式更接近矩阵的定义，并且在处理数据输入时，也按照了矩阵的形式来输入，界面更直观友好。
此外，在数据量较大时，该种方式在计算矩阵的 Hadamard 乘积时，代码执行效率更高。复杂度n*n

相反，本人下面的处理方式，仅仅使用了一维数组，并且严重依赖python本身的语法糖！
如果使用C语言，该种方法将不成立。
此外，在计算矩阵的 Hadamard 乘积时，复杂度较高。复杂度n*n*n*n。足足比官方答案提高了一倍！
'''

n = int(input("Enter the value of n: "))
A = [int(x) for x in input("Enter values for the Matrix A: \n").split()]
B = [int(x) for x in input("Enter values for the Matrix B: \n").split()]
C = [m*n for i,m in enumerate(A) for j,n in enumerate(B) if i == j]
print("After matrix multiplication: ")
print('-' * 7 * n)
x = 0
for i in C:
    print(i, end = '\t')
    x += 1
    if x == n:
        print()
        x = 0
print('-' * 7 * n)

############################################
'''
【实验楼的官方答案】
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)
'''
