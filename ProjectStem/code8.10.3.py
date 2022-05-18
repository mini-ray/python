terms = ["Bandwidth", "Hierarchy", "IPv6", "Software", "Firewall", "Cybersecurity", "Lists", "Program", "Logic", "Reliability"]
print(terms)

def swap(li,x,y):
	li[y],li[x] = li[x],li[y]
	return li,x,y

swap(terms,1,5)
swap(terms,2,4)
swap(terms,3,5)
swap(terms,5,6)
swap(terms,6,8)
swap(terms,8,9)
print(terms)