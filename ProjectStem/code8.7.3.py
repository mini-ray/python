w = ["Algorithm", "Logic", "Filter", "Software", "Network", "Parameters", "Analyze", "Algorithm", "Functionality", "Viruses"]

s = []

for i in range(len(w)):
	s.append (len(w[i]))
	
for j in range(len(w)):
	print (str(s[j]) + ": " + w[j])