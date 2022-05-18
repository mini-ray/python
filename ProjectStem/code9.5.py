a = [[34,38,50,44,39], 
     [42,36,40,43,44], 
     [24,31,46,40,45], 
     [43,47,35,31,26],
     [37,28,20,36,50]]

sum = 0
l = 0

for r in range(len(a)):
	for c in range(len(a)):
		sum = sum + a[r][c]
		l = l + 1
v = sum/l
print("Sum of all values: " + str(sum))
print("")
print("Average of all values: " + str(v))