def GPAcalc(x):
	#x = x.upper()
	if (x == "a" or x == "A"):
		x = 4
		print("Your GPA score is: " + str(x))
	elif (x == "b" or x == "B"):
		x = 3
		print("Your GPA score is: " + str(x))
	elif (x == "c" or x == "C"):
		x = 2
		print("Your GPA score is: " + str(x))
	elif (x == "d" or x == "D"):
		x = 1
		print("Your GPA score is: " + str(x))
	elif (x == "f" or x == "F"):
		x = 0
		print("Your GPA score is: " + str(x))
	else:
		x = "Invalid"
		print("Your GPA score is: " + str(x))
	return x

#MAIN

y = input("Enter your Letter Grade: ")

print(GPAcalc(y))
