petsNum = 0
rock = "rock"
pet = ""
while(pet != rock):
	pet = input("What pets do you have ")
	petsNum += 1
	if(pet != rock):
		print("You have a " + pet + " with a total of " + str(petsNum) + " pet(s)")
