import random
r = 0
a = 0
x = 0


while r == 0:
	while x == 0:
		n = random.randint(1,100)
		x = 1
	while a != "r":
		g = int(input("Guess the number:"))
		if g < n:
			print("Too low")
			a = "tl"
			break
		if g > n:
			print("Too high")
			a = "th"
			break
		if g == n:
			print("Correct")
			a = "r"
		if a == "r":
			nr = input("If you would like to play again please type 'yes' if not please type 'no'")
		if nr == "Yes" or nr == "yes":
			x = 0
		if nr == "No" or nr == "no":
			print("Ok bye")
			break
