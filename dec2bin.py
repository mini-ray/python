def dec2bin(n):
		binValue = bin(n)
		bs = str(bin(n))
		b = bs.replace('0b','')
		return b
		
def main():
		bString = dec2bin(10)
		print("\t",10, bString)
		bString = dec2bin(245)
		print("\t",245, bString)
		bString = dec2bin(65521)
		print("\t",65521, bString)
		bString = dec2bin(1023)
		print("\t",1023, bString)
		
main()