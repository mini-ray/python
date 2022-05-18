def findIt(v,num):
	for i in range(len(v)):
		if (v[i] == num):
			return i
	return -1

v = [24, 20, 29, 32, 34, 29, 49, 46, 39, 23, 42, 24, 38]

num = int(input("search for: "))
print(findIt(v,num))