import random
def buildArray(x,y):
	for i in range(y):
		x.append(random.randint(10,99))

x = []
num = int(input("How many values to add to the array: "))
buildArray(x,num)
print(x)