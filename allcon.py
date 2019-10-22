# basecon.py D04 CMC CWC

num = int(input("Enter a number: "))

def bincon(num):
	n = num
	#s = addSpace
	#print(n,s) #debug
	#print(n," = ",end="")
	d = 128
	binString ="" #create a stringcalled binString
	for i in range(0,8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString+str(q)
		if i == 3:
			binString = binString + " "
	#print(binString)
	return binString


# dechex.py D04 CMC kenny
def hexcon(num):
	key = "0123456789abcdef" 
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h


#charcon D04 iml
def charcon(num):
	charString = ""
	
	if num > 31 and num < 128:
		charString = chr(num)
		if num == 32:
			charString = "SPACE"
		if num == 127:
			charString = "DEL"
		
		charString = ", " + charString
			
	return charString


def main():
	#bincon(152,1)
	#bincon(191,0)
	#bincon(7,1)
		#bs = ""
		#for i in range(0,256):
				#bs = bincon(i,1)
				#hs = ""
				#hs = hexcon(i)
				#print(i,bs,hs,)
	dec =str(num)
	hex = hexcon(num)
	bin = bincon(num)
	char = charcon(num)

	print(dec,hex,bin,char)


main()
