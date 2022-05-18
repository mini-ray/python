N = []
v = [1,2,3,4,5]

for i in range(4):
	N.append(v)

def printIt(N):
	for r in range(len(N)):
		for c in range(len(N[0])):
			print((N[r][c]), end = " ")
		print("")

printIt(N)
print(" ")
N[0] = [1,1,1,1,1]
N[1] = [2,2,2,2,2]
N[2] = [3,3,3,3,3]
N[3] = [4,4,4,4,4]
	
printIt(N)