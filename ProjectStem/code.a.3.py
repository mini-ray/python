import random
ai = random.randint(0,1)
if ai == 0:
	name = input("Hello,my name is Bob, what is your name? ")
else:
	name = input("Hello,my name is Larry, what is your name? ")
check = input("Your name is " + name + "? y/n ")
if check == "n":
	name = input("Will you tell me your name? y/n ")
	if name == "y":
		name = input("What is your name? ")
	else:
		name = "Walter"
		print("I will call you Walter.")
print("Nice to meet you " + name + ".")
status = input("Will you be my friend" + name + "? y/n/m ")
if status == "y":
	print("I'm happy that you are my friend :)")
elif status == "n":
	print("Oh, OK :(")
else:
	print("I hope that we can become friends. :)")
nextime = input("Would you like to talk again? y/n/m ")
if nextime == "y":
	print("I would like to see you again aswell" + name + ". :)")
elif nextime == "n":
	print("Oh, so long then " + name + ". :(")
else:
	print("I hope that we have the ability to talk to each other again aswell.")
print("Do to the lack of programming that the developer is capable of doing, the conversation has ended.")
print("Have a good day.")
