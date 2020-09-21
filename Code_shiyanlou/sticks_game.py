print("There are 21 sticks, you can take 1~4 number of sticks at a time.")
print("Whoever will take the last stick will lose")

sticks = 21
while True:
	print("Sticks left: {}".format(sticks))
	if sticks == 1:
		print('you took the last stick, you lose')
		break
	sticks_taken = int(input("Take sticks(1~4): "))
	if sticks_taken >= 5 or sticks_taken <= 0:
		print("Wrong Choice")
	print("Computer took: {}".format(5 - sticks_taken))
	sticks -= 5
