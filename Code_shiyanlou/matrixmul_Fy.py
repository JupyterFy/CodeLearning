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
