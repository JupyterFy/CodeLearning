days = int(input("Enter days: "))
#divmod(num1, num2) 返回一个元组，这个元组包含两个值，第一个是 num1 和 num2 相整除得到的值，第二个是 num1 和 num2 求余得到的值，然后我们用 * 运算符拆封这个元组，得到这两个值。
print("Months = {} Days = {}".format(*divmod(days, 30)))
