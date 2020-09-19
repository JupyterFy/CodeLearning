sum = 0
a = int(input('Enter an interger: '))
for i in range(1,a+1):
    sum += 1.0/i
    print("{:2d} {:6.4f}".format(i, sum))
