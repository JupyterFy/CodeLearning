rows = int(input("Enter the number of rows: "))
n = rows
while n >= 0:
    x = ' ' * (rows - n)
    y = '*' * n
    n -= 1
    print(x + y)
