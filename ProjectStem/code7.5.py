def GPAcalc(lg,w):
	if (lg == "a" or lg == "A"):
		lg = 4
	elif (lg == "b" or lg == "B"):
		lg = 3
	elif (lg == "c" or lg == "C"):
		lg = 2
	elif (lg == "d" or lg == "D"):
		lg = 1
	elif (lg == "f" or lg == "F"):
		lg = 0
	else:
		lg = "Invalid"
		print("Your GPA score is: " + str(lg))
	if(w == 1 and lg != "Invalid"):
	    lg = lg + 1
	elif(w == 0 and lg != "Invalid"):
	    lg = lg + 0
	    #print("Your GPA score is: " + str(lg))
	else:
	    print("Your GPA score is: Invalid")
	
	#print("Your GPA score is: " + str(lg))
	return lg

def GPAavg(num):
    sum = 0
    for i in range(num):
        lg = (input("Enter your Letter Grade: "))
        w = int(input("Is it weighted? (1 = yes, 0 = no) "))
        GPAcalc(lg,w)
        if(GPAcalc(lg,w) == "Invalid"):
            print("Invalid")
            end=""
        else:
            sum = sum + GPAcalc(lg,w)
    return (sum / num)

#MAIN
num = int(input("How many Classes are you taking? "))
print("")
print("\nYour weighted GPA is " + str(GPAavg(num)))