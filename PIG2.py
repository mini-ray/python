# PIG2.py D04 
import random
from colorama import Fore, Back, Style
acp = 0 #all computer points
app = 0 #all player points
cp = 0  #computer points
pp = 0  #player points
t = 0   #turn



while (acp < 100 and app < 100):
	cp = 0
	pp = 0
	#player
	while (t != "y"):
		#roll
		pr = random.randint(1,6)
		print(Fore.BLUE + Style.BRIGHT + "Die Roll = " + str(pr))
		if pr == 1:
			t = "y"
			print(Fore.CYAN + Style.BRIGHT + "Your score:" + str(app))
			break
		pp = pp + pr
		print(Fore.BLUE + Style.BRIGHT + "Losable Points = " + str(pp))
		t = input(str(Fore.BLUE + Style.BRIGHT + "Hold? (y/n): "))
		if t == "y":
			app = app + pp
			print(Fore.CYAN + Style.BRIGHT + "Your score:" + str(app))
			break
	#computer		
	while t != 1:
		#roll
		cr = random.randint(1,6)
		if cr == 1:
			t = 1
			print(Fore.RED + Style.BRIGHT + "Computer Score:" + str(acp))
			break
		cp = cp + cr
		t = random.randint(1,3)
		if t == 1:
			acp = acp + cp
			print(Fore.RED + Style.BRIGHT + "Computer Score:" + str(acp))
if app >= 100:
	print(Fore.BLUE + Style.BRIGHT + "Your score:" + str(app))
	print(Fore.RED + Style.BRIGHT + "Computer Score:" + str(acp))
	print(Fore.YELLOW + Style.BRIGHT + "GG you win!")
else:
	print(Fore.BLUE + Style.BRIGHT + "Your score:" + str(app))
	print(Fore.RED + Style.BRIGHT + "Computer Score:" + str(acp))
	print(Fore.YELLOW + Style.BRIGHT + "You lose :(")
