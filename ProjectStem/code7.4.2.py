def GPAcalc(x,z):
	if (x == "a" or x == "A"):
		x = 4
	elif (x == "b" or x == "B"):
		x = 3
	elif (x == "c" or x == "C"):
		x = 2
	elif (x == "d" or x == "D"):
		x = 1
	elif (x == "f" or x == "F"):
		x = 0
	else:
		x = "Invalid"
		#print("Your GPA score is: " + str(x))
	if(z == 1 and x != "Invalid"):
	    x = x + 1
	    print("Your GPA score is: " + str(x))
	elif(z == 0 and x != "Invalid"):
	    x = x + 0
	    print("Your GPA score is: " + str(x))
	else:
	    print("Your GPA score is: Invalid")
	return x

#MAIN

y = input("Enter your Letter Grade: ")
z = int(input("Is it weighted? (1 = yes, 0 = no) "))
(GPAcalc(y,z))